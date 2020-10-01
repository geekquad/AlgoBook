#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;


void knapsack(vector<pair <double, double>>& items, double maxW, double numItems) {
	vector <vector <double>> table;

	for (double i = 0; i < numItems + 1; ++i)
		table.push_back(vector<double>(maxW + 1));

	for (double i = 0; i < table[0].size(); ++i)//first row == 0
		table[0][i] = 0;
	for (double i = 0; i < table.size(); ++i)//first col == 0
		table[i][0] = 0;

	for (double i = 1; i < table.size(); ++i)
		for (double w = 1; w < table[0].size(); w++) {
			if (items[i - 1].second <= w)
				table[i][w] = max(table[i - 1][w], items[i - 1].first + table[i - 1][w - items[i - 1].second]);
			else
				table[i][w] = table[i - 1][w];
		}

	cout << "Best Value: " << table[numItems][maxW] << endl << endl;
	cout << "Objects Used: (Value, Weight) " << endl;

	double w = maxW;
	/*for (auto i : table) {
		for (auto j : i) {
			cout << j << " ";
		}
		cout << endl;
	}*/

	//print objects to get
	for (double i = numItems; i > 0 && w > 0; i--) {
		if (table[i][w] == table[i - 1][w])
			continue;
		else {
			cout << items[i - 1].first << " " << items[i - 1].second << endl;
			w -= items[i - 1].second;
		}
	}
}


// first is val, second is weight
int main() {
	double maxW, numItems;

	cout << "Enter Max Weight and Number of objects: ";
	cin >> maxW;
	cin >> numItems;

	vector <pair<double, double>> items;
	for (double i = 0; i < numItems; ++i) {
		cout << "Enter Value then weight: ";
		pair<double, double> p;
		cin >> p.first >> p.second;
		items.emplace_back(p);
	}

	sort(items.begin(), items.end(), [](auto p1, auto p2) {/*return double(p1.first) / p1.second > double(p2.first) / p2.second;*/
		return double(p1.second) < double(p2.second); });
	knapsack(items, maxW, numItems);

	return 0;
}