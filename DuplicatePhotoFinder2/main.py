from DuplicateRemover import DuplicateRemover


dirname = "dataset"

# Remove Duplicates
dr = DuplicateRemover(dirname)
dr.find_duplicates()

# Find Similar Images
dr.find_similar("p3.jpg",10)
    