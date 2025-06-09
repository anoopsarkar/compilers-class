import tkinter as tk
from nltk.tree import Tree

def measure_tree_width(tree, node_width=60, spacing=20):
    if isinstance(tree, str):
        return node_width
    child_widths = [measure_tree_width(child, node_width, spacing) for child in tree]
    return max(node_width, sum(child_widths) + spacing * (len(tree) - 1))

def draw_node(canvas, x, y, text, padx=10, pady=5):
    font = ('Helvetica', 12)
    temp_id = canvas.create_text(x, y, text=text, font=font, anchor='center')
    bbox = canvas.bbox(temp_id)
    canvas.delete(temp_id)

    if bbox:
        x0, y0, x1, y1 = bbox
        x0 -= padx
        x1 += padx
        y0 -= pady
        y1 += pady
        canvas.create_rectangle(x0, y0, x1, y1, fill='lightblue', outline='black')
        canvas.create_text(x, y, text=text, font=font, fill='black')
        return (x0, y0, x1, y1)
    return None

def draw_nltk_tree(canvas, tree, x, y, spacing_x=20, spacing_y=80):
    subtree_width = measure_tree_width(tree, spacing=spacing_x)
    bbox = draw_node(canvas, x, y, tree.label() if isinstance(tree, Tree) else tree)
    if bbox:
        x0, y0, x1, y1 = bbox
        parent_bottom = (x, y1)

    if isinstance(tree, str):
        return subtree_width

    child_x = x - subtree_width // 2
    for child in tree:
        this_subtree_width = measure_tree_width(child, spacing=spacing_x)
        child_center_x = child_x + this_subtree_width // 2
        child_center_y = y + spacing_y

        draw_nltk_tree(canvas, child, child_center_x, child_center_y, spacing_x, spacing_y)

        child_bbox = draw_node(canvas, child_center_x, child_center_y, child.label() if isinstance(child, Tree) else child)
        if child_bbox:
            cx0, cy0, cx1, cy1 = child_bbox
            canvas.create_line(parent_bottom[0], parent_bottom[1], (cx0 + cx1) // 2, cy0)

        child_x += this_subtree_width + spacing_x

    return subtree_width

### GUI Setup for Multiple Trees ###
class TreeViewer:
    def __init__(self, root, trees):
        self.root = root
        self.trees = trees
        self.index = 0

        self.canvas = tk.Canvas(root, width=1200, height=800, bg='white')
        self.canvas.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.prev_button = tk.Button(btn_frame, text="Previous", command=self.show_prev)
        self.prev_button.pack(side='left', padx=5)

        self.next_button = tk.Button(btn_frame, text="Next", command=self.show_next)
        self.next_button.pack(side='left', padx=5)

        self.status_label = tk.Label(btn_frame, text="")
        self.status_label.pack(side='left', padx=10)

        self.show_tree()

    def show_tree(self):
        self.canvas.delete("all")
        if self.trees:
            draw_nltk_tree(self.canvas, self.trees[self.index], 600, 50, spacing_x=30, spacing_y=80)
            self.status_label.config(text=f"Tree {self.index + 1} of {len(self.trees)}")

    def show_prev(self):
        if self.index > 0:
            self.index -= 1
            self.show_tree()

    def show_next(self):
        if self.index < len(self.trees) - 1:
            self.index += 1
            self.show_tree()

def draw(trees, title):
    root = tk.Tk()
    root.title(title)

    # Draw tree starting at the center top
    app = TreeViewer(root, trees)
    root.mainloop()
#    draw_nltk_tree(canvas, example_tree, x=600, y=50, spacing_x=30, spacing_y=80)
#    root.mainloop()

if __name__ == '__main__':
    ### Example usage ###
    trees = [
        Tree.fromstring("(S (NP (DT The) (NN cat)) (VP (VBD sat)))"),
        Tree.fromstring("(S (NP (DT The) (JJ big) (NN cat)) (VP (VBD sat) (PP (IN on) (NP (DT the) (NN mat)))))"),
        Tree.fromstring("(S (NP (DT A) (JJ quick) (JJ brown) (NN fox)) (VP (VBD jumped) (PP (IN over) (NP (DT the) (JJ lazy) (NN dog)))))")
    ]
    draw(trees, "draw trees")

