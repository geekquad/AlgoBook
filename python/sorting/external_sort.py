import math
import sys
import generator_random_data as grd
import memory_chunk_module as mcm


class FileSplitter(object):
    chunk_filenames = []

    def __init__(self, filename, chunk_filename_format):
        self.filename = filename
        self.chunk_filename_format = chunk_filename_format

    def write_chunk(self, data, chunk_number):
        filename = self.chunk_filename_format.format(chunk_number)
        file = open(filename, 'w')
        file.write(data)
        file.close()
        FileSplitter.chunk_filenames.append(filename)

    def get_chunk_filenames(self):
        return self.chunk_filenames

    def split(self, chunk_memory):
        file = open(self.filename, 'r')
        i = 0

        while True:
            lines = file.readlines(chunk_memory)
            if lines == []:
                break

            lines.sort()

            self.write_chunk(''.join(lines), i)
            i += 1


class MergeSortFile(object):
    def __init__(self, total_files):
        self.total_files = total_files

    def select(self, choices):
        min_index = -1
        min_str = None

        temp_array = []

        for choice in choices:
            if(choice != ''and choice != '\n'):
                temp_array.append(int(choice))

        for i in range(self.total_files):
            if min_str is None:
                if i in choices:
                    min_str = choices[i]
                    min_index = i

            if i in choices:
                if int(min_str) > int(choices[i]):
                    min_str = choices[i]
                    min_index = i

        return min_index


class FilesArray(object):
    def __init__(self, files):
        self.files = files
        self.empty = set()
        self.num_buffers = len(files)
        self.buffers = {i: None for i in range(self.num_buffers)}

    def get_dict(self):
        return {i: self.buffers[i] for i in range(self.num_buffers) if i not in self.empty}

    def refresh(self):
        for i in range(self.num_buffers):
            if self.buffers[i] is None and i not in self.empty:
                self.buffers[i] = self.files[i].readline()

                if self.buffers[i] == '':
                    self.empty.add(i)

        if len(self.empty) == self.num_buffers:
            return False

        return True

    def clean_buffer(self, index):
        value = self.buffers[index]
        self.buffers[index] = None

        return value


class FileMerger(object):
    def __init__(self, merger):
        self.merger = merger

    def merge(self, filenames, outfilename, buffer_size):
        outfile = open(outfilename, 'w', int(math.ceil(buffer_size)))
        buffers = FilesArray(self.get_file_handles(filenames, buffer_size))

        while buffers.refresh():
            min_index = self.merger.select(buffers.get_dict())
            outfile.write(buffers.clean_buffer(min_index))

    def get_file_handles(self, filenames, buffer_size):
        files = {}
        for i in range(len(filenames)):
            files[i] = open(filenames[i], 'r', int(math.ceil(buffer_size)))

        return files


class FileSplitSort(object):
    def __init__(self, chunk_memory, cleanup):
        self.chunk_memory = chunk_memory
        self.cleanup = cleanup

    def sort_data(self, filename, chunk_filename_format):
        total_chunks = mcm.get_total_chunk(filename, self.chunk_memory)
        file_splitter = FileSplitter(filename, chunk_filename_format)
        file_splitter.split(self.chunk_memory)

        file_merger = FileMerger(MergeSortFile(total_chunks))
        buffer_merge_size = self.chunk_memory / (total_chunks)

        output_filename = filename.replace(".txt", "") + '_sorted.txt'
        file_merger.merge(file_splitter.get_chunk_filenames(), output_filename, buffer_merge_size)

        if self.cleanup:
            mcm.cleanup_chunk_file(FileSplitter.chunk_filenames)


def sort_as_chunk(filename, memory_of_chunk, cleanup_chunk_flag, chunk_filename_format = "age_sorted_{0}.txt"):
    filesort = FileSplitSort(mcm.get_parsed_memory(memory_of_chunk), cleanup_chunk_flag)
    filesort.sort_data(filename, chunk_filename_format)
    print("sorting data: success")


if __name__ == "__main__":
    filename = "age.txt"

    # Demo
    # grd.create_file(filename, 10000, 16, 59)
    # sort_as_chunk(filename, "20K", True)
