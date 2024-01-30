import traceback
import os

if __name__ == '__main__':
    try:
        pwd = os.path.dirname(__file__)
        root_path = os.path.dirname(pwd)
        print(root_path)

        filepath = f"{root_path}\\kindle_total_clippings\\My Clippings_20240126.txt"
        with open(filepath, 'r', encoding="utf8") as f:
            contents = f.readlines()

        contents = [content.replace('\n', '') for content in contents]
        print(contents)
        
        #book_name = "Head First Git"
        book_name = "_OceanofPDF.com_Screenplay_-_Syd_Field (Syd Field)"
        print(f"book_name - {book_name}")

        line_indices_matching_book = []
        for ind, line in enumerate(contents):
            if book_name in line:
                line_indices_matching_book.append(ind)
        
        print(f"line_indices_matching_book - {line_indices_matching_book}")

        highlights_lst = []
        for ind in line_indices_matching_book:
            tracker_ind = ind+1
            one_highlight_lst = []
            while True:
                if contents[tracker_ind] != '==========':    # Check if the highlight has ended
                    one_highlight_lst.append(contents[tracker_ind])
                    #print(contents[tracker_ind])
                else:
                    break
                tracker_ind += 1
            one_highlight_str = '\n'.join(one_highlight_lst)
            print(f"one_highlight_str - {one_highlight_str}")
            highlights_lst.append(one_highlight_str)

        print(f"highlights_lst - {highlights_lst}")

        book_highlight_path = f"{root_path}\\bookwise_highlights\\{book_name}"
        if not os.path.exists(book_highlight_path):
            os.makedirs(book_highlight_path)
        with open(f"{book_highlight_path}/highlights.txt", 'w', encoding="utf8") as f:
            for highlight in highlights_lst:
                f.write(highlight + '\n')
    except Exception as e:
        print(e)
        print(traceback.format_exc())