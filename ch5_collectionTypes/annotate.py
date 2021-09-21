### Before
# def create_author_count_mapping(cookbooks: list) -> dict:
#     counter = defaultdict(lambda: 0)
#     for book in cookbooks:
#         counter[book.author] += 1
#     return counter

### After
AuthorToCountMapping = dict[str, int]
def create_author_count_mapping(
				cookbooks: list[Cookbook]
                               ) -> AuthorToCountMapping:
    counter = defaultdict(lambda: 0)
    for book in cookbooks:
        counter[book.author] += 1
    return counter