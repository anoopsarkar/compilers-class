import tkinter as tk
from tkinter import ttk
import nltk
from nltk.parse import ShiftReduceParser

class SimpleShiftReduceGUI:
    def __init__(self, grammar, sentence):
        self.grammar = grammar
        self.sentence = sentence
        self.parser = ShiftReduceParser(grammar)
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Shift-Reduce Parser")
        self.root.geometry("800x600")
        
        # Create interface
        self.create_widgets()
        
        # Parse and show results
        self.parse_sentence()
    
    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Shift-Reduce Parser", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Sentence display
        sent_frame = tk.Frame(self.root)
        sent_frame.pack(pady=5)
        tk.Label(sent_frame, text="Sentence:", font=("Arial", 12, "bold")).pack(side=tk.LEFT)
        tk.Label(sent_frame, text=" ".join(self.sentence), font=("Arial", 12)).pack(side=tk.LEFT)
        
        # Grammar display
        grammar_frame = tk.LabelFrame(self.root, text="Grammar Rules", font=("Arial", 10, "bold"))
        grammar_frame.pack(pady=10, padx=10, fill=tk.BOTH)
        
        grammar_text = tk.Text(grammar_frame, height=8, width=60, font=("Courier", 10))
        grammar_text.pack(pady=5, padx=5)
        
        for rule in self.grammar.productions():
            grammar_text.insert(tk.END, f"{rule}\n")
        grammar_text.config(state=tk.DISABLED)
        
        # Parse results
        self.result_frame = tk.LabelFrame(self.root, text="Parse Results", font=("Arial", 10, "bold"))
        self.result_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Add scrollable text area for results
        text_frame = tk.Frame(self.result_frame)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.result_text = tk.Text(text_frame, font=("Courier", 10))
        scrollbar = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scrollbar.set)
        
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        parse_btn = tk.Button(button_frame, text="Re-parse", command=self.parse_sentence)
        parse_btn.pack(side=tk.LEFT, padx=5)
        
        quit_btn = tk.Button(button_frame, text="Quit", command=self.root.quit)
        quit_btn.pack(side=tk.LEFT, padx=5)
    
    def parse_sentence(self):
        self.result_text.delete(1.0, tk.END)
        
        try:
            # Parse with tracing
            self.result_text.insert(tk.END, "Parsing with shift-reduce algorithm...\n")
            self.result_text.insert(tk.END, "=" * 50 + "\n\n")
            
            # Capture parser trace
            import io
            import sys
            
            # Redirect stdout to capture trace
            old_stdout = sys.stdout
            sys.stdout = captured_output = io.StringIO()
            
            try:
                parser_with_trace = ShiftReduceParser(self.grammar, trace=2)
                trees = list(parser_with_trace.parse(self.sentence))
            finally:
                sys.stdout = old_stdout
            
            # Show the trace
            trace_output = captured_output.getvalue()
            if trace_output:
                self.result_text.insert(tk.END, "Parsing steps:\n")
                self.result_text.insert(tk.END, "-" * 20 + "\n")
                self.result_text.insert(tk.END, trace_output)
                self.result_text.insert(tk.END, "\n")
            
            # Show parse trees
            if trees:
                self.result_text.insert(tk.END, f"\nFound {len(trees)} parse tree(s):\n")
                self.result_text.insert(tk.END, "=" * 30 + "\n")
                
                for i, tree in enumerate(trees):
                    self.result_text.insert(tk.END, f"\nParse Tree {i+1}:\n")
                    self.result_text.insert(tk.END, str(tree) + "\n")
                    
                    # Show tree in a more readable format
                    self.result_text.insert(tk.END, "\nTree structure:\n")
                    tree_str = self.format_tree(tree, 0)
                    self.result_text.insert(tk.END, tree_str + "\n")
            else:
                self.result_text.insert(tk.END, "\nNo parse trees found!\n")
                self.result_text.insert(tk.END, "Check if your grammar covers the sentence.\n")
                
        except Exception as e:
            self.result_text.insert(tk.END, f"\nError during parsing: {e}\n")
            import traceback
            self.result_text.insert(tk.END, traceback.format_exc())
    
    def format_tree(self, tree, indent=0):
        """Format tree in a readable indented format"""
        result = "  " * indent + str(tree.label()) + "\n"
        
        for child in tree:
            if hasattr(child, 'label'):  # It's a subtree
                result += self.format_tree(child, indent + 1)
            else:  # It's a leaf (terminal)
                result += "  " * (indent + 1) + f"'{child}'\n"
        
        return result
    
    def mainloop(self):
        self.root.mainloop()

# Example usage
if __name__ == "__main__":
    # Your grammar and sentence
    grammar = nltk.CFG.fromstring("""
        S -> NP VP
        VP -> V NP
        NP -> Det N | 'Mary' | 'Bob'
        Det -> 'the'
        N -> 'dog' | 'cat'
        V -> 'saw'
    """)
    
    sent = "Mary saw Bob".split()
    
    # Create and run the GUI
    app = SimpleShiftReduceGUI(grammar, sent)
    app.mainloop()
