from __future__ import print_function
import collections
import itertools
import random

import graphviz

# Types::
# Node: str
# Graph: {Node: set(Node)} aka adjacency list
# Terminals: set(Node)
# Edge: frozenset([Node, Node])
# Tree: set(Edge) aka edge list, used for steiner solution
# Path: [Node]
# ShortestPath: {(Node, Node): Path}

def render_graph(g):
    dot = graphviz.Graph()
    for v0, v1 in get_edges_from_graph(g):
        dot.edge(v0, v1)
    dot.render('graph.gv')

def get_edges_from_graph(g):
    edges = set()
    for v, es in g.items():
        for e in es:
            edges.add(frozenset((v, e)))
    return edges

def render_steiner_solution(g, terminals, tree_edges):
    terminal_style = {'color': 'blue'}
    steiner_style = {'color': 'red'}
    def get_steiner_nodes(terminals, tree_edges):
        ns = set()
        for e0, e1 in tree_edges:
            ns.add(e0)
            ns.add(e1)
        return ns - set(terminals)
    def get_node_style(v, terminals, steiner_nodes):
        if v in terminals:
            return terminal_style
        elif v in steiner_nodes:
            return steiner_style
        return {}
    def get_edge_style(e, tree_edges):
        if e in tree_edges:
            return steiner_style
        return {}
    dot = graphviz.Graph()
    steiner_nodes = get_steiner_nodes(terminals, tree_edges)
    for v, es in g.items():
        dot.node(v, **get_node_style(v, terminals, steiner_nodes))
    for v0, v1 in get_edges_from_graph(g):
        dot.edge(v0, v1, **get_edge_style(frozenset((v0, v1)), tree_edges))
    dot.render('graph.gv')

def create_random_graph(n, p):
    vs = [str(i) for i in range(n)]
    edge_count = int(round(p*(n-1)*n/2))
    es = sample_iterable(generate_all_possible_edges(vs), edge_count)
    g = {v: [] for v in vs}
    for v0, v1 in es:
        g[v0].append(v1)
        g[v1].append(v0)
    return connect_components(get_connected_components(g))

def get_connected_components(g):
    components = []
    unvisited = set(g)
    while unvisited:
        component = {}
        queue = collections.deque(random.sample(unvisited, 1))
        while queue:
            cur_node = queue.popleft()
            component[cur_node] = g[cur_node]
            if cur_node not in unvisited: continue
            for neighbor in g[cur_node]:
                if neighbor in unvisited:
                    queue.append(neighbor)
            unvisited.remove(cur_node)
        components.append(component)
    return components

def connect_components(gs):
    ret = {}
    for g in gs:
        ret.update(g)
    for g0, g1 in zip(gs, gs[1:]):
        v0 = random.sample(list(g0), 1)[0]
        v1 = random.sample(list(g1), 1)[0]
        ret[v0].append(v1)
        ret[v1].append(v0)
    return ret

def generate_all_possible_edges(vs):
    for i, v0 in enumerate(vs):
        for v1 in vs[i+1:]:
            yield (v0, v1)

def sample_iterable(iterable, samplesize):
    results = []
    iterator = iter(iterable)
    # Fill in the first samplesize elements:
    try:
        for _ in range(samplesize):
            results.append(next(iterator))
    except StopIteration:
        raise ValueError('Sample larger than population.')
    random.shuffle(results)  # Randomize their positions
    for i, v in enumerate(iterator, samplesize):
        r = random.randint(0, i)
        if r < samplesize:
            results[r] = v  # at a decreasing rate, replace random items
    return results

def pick_random_terminals(g):
    n = len(g) // 3
    return frozenset(random.sample(list(g), n))

def get_steiner_tree(g, Y):
    q = random.sample(Y, 1)[0]
    C = Y - {q}
    dij = all_pairs_shortest_paths(g)
    S = get_steiner_base_case(dij)
    SkD = {}
    for i in range(2, len(Y)):
        for Dtup in itertools.combinations(C, i):
            D = frozenset(Dtup)
            for k in g:
                E_and_F_trees = []
                for E, F in algorithm_u(Dtup, 2):
                    E_and_F_trees.append((S[frozenset([k]+E)], S[frozenset([k]+F)]))
                SkD[(k, D)] = min(E_and_F_trees, key=lambda x: len(x[0]) + len(x[1]))
            for m in {q} if D == C else g:
                lengths_and_k_and_tree = []
                for k in g:
                    lengths_and_k_and_tree.append((len(dij[(m, k)]) + len(SkD[(k, D)][0]) + len(SkD[(k, D)][1]),
                                                   k,
                                                   node_and_path_to_edges(m, dij[(m,k)]).union(SkD[(k, D)][0]).union(SkD[(k, D)][1])))
                length, k, tree = min(lengths_and_k_and_tree, key=lambda x: x[0])
                S[frozenset(D.union(frozenset([m])))] = tree
    return S[frozenset(Y)]

def node_and_path_to_edges(v, p):
    edges = [frozenset([e0, e1]) for e0, e1 in zip([v] + p, p)]
    return frozenset(edges)

def get_steiner_base_case(dij):
    b = {}
    for (v0, v1), p in dij.items():
        b[frozenset([v0, v1])] = node_and_path_to_edges(v0, p)
    return b

def all_pairs_shortest_paths(g):
    d = {}
    for v in g:
        d.update(single_source_shortest_paths(g, v))
    return d

def single_source_shortest_paths(g, s):
    d = {(s, v): [] for v in g}
    unvisited = set(g)
    queue = collections.deque([s])
    while queue:
        current = queue.popleft()
        if current not in unvisited: continue
        for neighbor in g[current]:
            if neighbor in unvisited:
                path = d[(s, current)]
                dist = len(path)
                neighbor_dist = len(d[(s, neighbor)])
                if dist+1 < neighbor_dist or neighbor_dist == 0:
                    d[(s, neighbor)] = path + [neighbor]
                queue.append(neighbor)
        unvisited.remove(current)
    for v in unvisited:
        del d[(s, v)]
    return d

def algorithm_u(ns, m):
    def visit(n, a):
        ps = [[] for i in range(m)]
        for j in range(n):
            ps[a[j + 1]].append(ns[j])
        return ps

    def f(mu, nu, sigma, n, a):
        if mu == 2:
            yield visit(n, a)
        else:
            for v in f(mu - 1, nu - 1, (mu + sigma) % 2, n, a):
                yield v
        if nu == mu + 1:
            a[mu] = mu - 1
            yield visit(n, a)
            while a[nu] > 0:
                a[nu] = a[nu] - 1
                yield visit(n, a)
        elif nu > mu + 1:
            if (mu + sigma) % 2 == 1:
                a[nu - 1] = mu - 1
            else:
                a[mu] = mu - 1
            if (a[nu] + sigma) % 2 == 1:
                for v in b(mu, nu - 1, 0, n, a):
                    yield v
            else:
                for v in f(mu, nu - 1, 0, n, a):
                    yield v
            while a[nu] > 0:
                a[nu] = a[nu] - 1
                if (a[nu] + sigma) % 2 == 1:
                    for v in b(mu, nu - 1, 0, n, a):
                        yield v
                else:
                    for v in f(mu, nu - 1, 0, n, a):
                        yield v

    def b(mu, nu, sigma, n, a):
        if nu == mu + 1:
            while a[nu] < mu - 1:
                yield visit(n, a)
                a[nu] = a[nu] + 1
            yield visit(n, a)
            a[mu] = 0
        elif nu > mu + 1:
            if (a[nu] + sigma) % 2 == 1:
                for v in f(mu, nu - 1, 0, n, a):
                    yield v
            else:
                for v in b(mu, nu - 1, 0, n, a):
                    yield v
            while a[nu] < mu - 1:
                a[nu] = a[nu] + 1
                if (a[nu] + sigma) % 2 == 1:
                    for v in f(mu, nu - 1, 0, n, a):
                        yield v
                else:
                    for v in b(mu, nu - 1, 0, n, a):
                        yield v
            if (mu + sigma) % 2 == 1:
                a[nu - 1] = 0
            else:
                a[mu] = 0
        if mu == 2:
            yield visit(n, a)
        else:
            for v in b(mu - 1, nu - 1, (mu + sigma) % 2, n, a):
                yield v

    n = len(ns)
    a = [0] * (n + 1)
    for j in range(1, m + 1):
        a[n - m + j] = j - 1
    return f(m, n, 0, n, a)

if __name__ == '__main__':
    g = create_random_graph(40, 0.10)
    terminals = pick_random_terminals(g)
    tree_edges = get_steiner_tree(g, terminals)
    render_steiner_solution(g, terminals, tree_edges)