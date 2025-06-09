import tkinter as tk
from tkinter import ttk, messagebox
import nltk
from nltk.parse import ShiftReduceParser
from nltk import CFG

class InteractiveShiftReduceGUI:
    def __init__(self, grammar, sentence):
        self.grammar = grammar
        self.sentence = sentence
        self.reset_parser_state()
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Interactive Shift-Reduce Parser")
        self.root.geometry("1000x700")
        
        # Create interface
        self.create_widgets()
        
        # Initialize display
        self.update_display()
    
    def reset_parser_state(self):
        """Reset the parser to initial state"""
        self.stack = []
        self.input_buffer = self.sentence.copy()
        self.step_number = 0
        self.parse_complete = False
        self.parse_successful = False
        self.action_history = []
        self.current_action = "Ready to start parsing"
    
    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Interactive Shift-Reduce Parser", 
                        font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Sentence display
        sent_frame = tk.Frame(self.root)
        sent_frame.pack(pady=5)
        tk.Label(sent_frame, text="Sentence:", font=("Arial", 12, "bold")).pack(side=tk.LEFT)
        tk.Label(sent_frame, text=" ".join(self.sentence), font=("Arial", 12)).pack(side=tk.LEFT)
        
        # Current state display
        state_frame = tk.LabelFrame(self.root, text="Current Parser State", 
                                   font=("Arial", 12, "bold"))
        state_frame.pack(pady=10, padx=10, fill=tk.X)
        
        # Stack display with detailed visualization
        stack_frame = tk.Frame(state_frame)
        stack_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(stack_frame, text="Stack:", font=("Arial", 11, "bold")).pack(side=tk.LEFT)
        
        # Stack contents with position numbers
        stack_display_frame = tk.Frame(stack_frame)
        stack_display_frame.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        self.stack_label = tk.Label(stack_display_frame, text="[ ]", font=("Courier", 11),
                                   bg="lightblue", relief=tk.SUNKEN, anchor=tk.W)
        self.stack_label.pack(fill=tk.X)
        
        # Stack positions (indices)
        self.stack_positions_label = tk.Label(stack_display_frame, text="", font=("Courier", 9),
                                             fg="gray", anchor=tk.W)
        self.stack_positions_label.pack(fill=tk.X)
        
        # Input buffer display with positions
        buffer_frame = tk.Frame(state_frame)
        buffer_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(buffer_frame, text="Input:", font=("Arial", 11, "bold")).pack(side=tk.LEFT)
        
        buffer_display_frame = tk.Frame(buffer_frame)
        buffer_display_frame.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        self.buffer_label = tk.Label(buffer_display_frame, text="", font=("Courier", 11),
                                    bg="lightgreen", relief=tk.SUNKEN, anchor=tk.W)
        self.buffer_label.pack(fill=tk.X)
        
        # Input buffer positions
        self.buffer_positions_label = tk.Label(buffer_display_frame, text="", font=("Courier", 9),
                                              fg="gray", anchor=tk.W)
        self.buffer_positions_label.pack(fill=tk.X)
        
        # Current action display
        action_frame = tk.Frame(state_frame)
        action_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(action_frame, text="Action:", font=("Arial", 11, "bold")).pack(side=tk.LEFT)
        self.action_label = tk.Label(action_frame, text="", font=("Arial", 11),
                                    bg="lightyellow", relief=tk.SUNKEN, anchor=tk.W)
        self.action_label.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        # Step number
        step_frame = tk.Frame(state_frame)
        step_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(step_frame, text="Step:", font=("Arial", 11, "bold")).pack(side=tk.LEFT)
        self.step_label = tk.Label(step_frame, text="0", font=("Arial", 11, "bold"),
                                  fg="blue")
        self.step_label.pack(side=tk.LEFT, padx=10)
        
        # Add visual stack representation
        visual_stack_frame = tk.LabelFrame(self.root, text="Visual Stack Representation", 
                                          font=("Arial", 10, "bold"))
        visual_stack_frame.pack(pady=5, padx=10, fill=tk.X)
        
        self.visual_stack_canvas = tk.Canvas(visual_stack_frame, height=100, bg="white")
        self.visual_stack_canvas.pack(fill=tk.X, padx=5, pady=5)
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.shift_btn = tk.Button(button_frame, text="SHIFT", command=self.shift_action,
                                  font=("Arial", 10, "bold"), bg="lightcoral", width=10)
        self.shift_btn.pack(side=tk.LEFT, padx=5)
        
        self.reduce_btn = tk.Button(button_frame, text="REDUCE", command=self.show_reduce_options,
                                   font=("Arial", 10, "bold"), bg="lightblue", width=10)
        self.reduce_btn.pack(side=tk.LEFT, padx=5)
        
        self.auto_step_btn = tk.Button(button_frame, text="AUTO STEP", command=self.auto_step,
                                      font=("Arial", 10, "bold"), bg="lightgreen", width=10)
        self.auto_step_btn.pack(side=tk.LEFT, padx=5)
        
        self.reset_btn = tk.Button(button_frame, text="RESET", command=self.reset_parser,
                                  font=("Arial", 10, "bold"), bg="orange", width=10)
        self.reset_btn.pack(side=tk.LEFT, padx=5)
        
        # Grammar display
        grammar_frame = tk.LabelFrame(self.root, text="Grammar Rules", 
                                     font=("Arial", 10, "bold"))
        grammar_frame.pack(pady=10, padx=10, fill=tk.BOTH)
        
        grammar_text = tk.Text(grammar_frame, height=6, font=("Courier", 9))
        grammar_scrollbar = tk.Scrollbar(grammar_frame, orient=tk.VERTICAL, 
                                       command=grammar_text.yview)
        grammar_text.configure(yscrollcommand=grammar_scrollbar.set)
        
        grammar_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        grammar_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add grammar rules with numbers
        for i, rule in enumerate(self.grammar.productions(), 1):
            grammar_text.insert(tk.END, f"{i:2d}. {rule}\n")
        grammar_text.config(state=tk.DISABLED)
        
        # History display
        history_frame = tk.LabelFrame(self.root, text="Action History", 
                                     font=("Arial", 10, "bold"))
        history_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        self.history_text = tk.Text(history_frame, height=8, font=("Courier", 9))
        history_scrollbar = tk.Scrollbar(history_frame, orient=tk.VERTICAL, 
                                       command=self.history_text.yview)
        self.history_text.configure(yscrollcommand=history_scrollbar.set)
        
        self.history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def update_display(self):
        """Update all display elements"""
        # Update stack display with positions
        if self.stack:
            stack_str = "[ " + " ".join(f"{item}" for item in self.stack) + " ]"
            # Create position indicators
            positions = []
            for i in range(len(self.stack)):
                # Calculate spacing for position numbers
                item_str = str(self.stack[i])
                positions.append(f"{i:^{len(item_str)}}")
            pos_str = "  " + " ".join(positions) + "  "
        else:
            stack_str = "[ ]"
            pos_str = ""
        
        self.stack_label.config(text=stack_str)
        self.stack_positions_label.config(text=pos_str)
        
        # Update input buffer display with positions
        if self.input_buffer:
            buffer_str = " ".join(self.input_buffer)
            # Create position indicators for input buffer
            positions = []
            for i, word in enumerate(self.input_buffer):
                positions.append(f"{i:^{len(word)}}")
            buffer_pos_str = " ".join(positions)
        else:
            buffer_str = "(empty)"
            buffer_pos_str = ""
        
        self.buffer_label.config(text=buffer_str)
        self.buffer_positions_label.config(text=buffer_pos_str)
        
        # Update visual stack representation
        self.update_visual_stack()
        
        # Update action display
        self.action_label.config(text=self.current_action)
        
        # Update step number
        self.step_label.config(text=str(self.step_number))
        
        # Update button states
        can_shift = len(self.input_buffer) > 0 and not self.parse_complete
        can_reduce = len(self.stack) > 0 and not self.parse_complete
        
        self.shift_btn.config(state=tk.NORMAL if can_shift else tk.DISABLED)
        self.reduce_btn.config(state=tk.NORMAL if can_reduce else tk.DISABLED)
        self.auto_step_btn.config(state=tk.NORMAL if not self.parse_complete else tk.DISABLED)
        
        # Check if parsing is complete
        if len(self.stack) == 1 and len(self.input_buffer) == 0 and str(self.stack[0]) == 'S':
            self.parse_complete = True
            self.parse_successful = True
            self.current_action = "✓ PARSING SUCCESSFUL! Sentence accepted."
            self.action_label.config(text=self.current_action, fg="green")
            messagebox.showinfo("Success!", "Parsing completed successfully!\nSentence is accepted by the grammar.")
#        elif len(self.input_buffer) == 0 and not self.parse_successful:
#            if len(self.stack) != 1 or str(self.stack[0]) != 'S':
#                self.parse_complete = True
#                self.current_action = "✗ PARSING FAILED! Cannot reduce to start symbol."
#                self.action_label.config(text=self.current_action, fg="red")
    
    def update_visual_stack(self):
        """Update the visual representation of the stack"""
        self.visual_stack_canvas.delete("all")
        canvas_width = self.visual_stack_canvas.winfo_width()
        canvas_height = self.visual_stack_canvas.winfo_height()
        
        if canvas_width <= 1:  # Canvas not initialized yet
            self.root.after(100, self.update_visual_stack)
            return
        
        if not self.stack:
            # Draw empty stack
            self.visual_stack_canvas.create_text(canvas_width//2, canvas_height//2,
                                               text="Stack is empty", font=("Arial", 12),
                                               fill="gray")
            return
        
        # Calculate dimensions for stack items
        num_items = len(self.stack)
        item_width = min(80, (canvas_width - 40) // max(1, num_items))
        item_height = 60
        start_x = (canvas_width - (num_items * item_width)) // 2
        
        # Draw stack items from bottom to top (left to right)
        for i, item in enumerate(self.stack):
            x = start_x + i * item_width
            y = canvas_height - item_height - 10
            
            # Determine colors based on item type
            if str(item) in [str(rule.lhs()) for rule in self.grammar.productions()]:
                # Non-terminal (grammar rule LHS)
                fill_color = "lightcoral"
                text_color = "darkred"
            else:
                # Terminal (word from sentence)
                fill_color = "lightblue"
                text_color = "darkblue"
            
            # Draw rectangle for stack item
            self.visual_stack_canvas.create_rectangle(x, y, x + item_width - 5, y + item_height,
                                                    fill=fill_color, outline="black", width=2)
            
            # Add text
            text_x = x + (item_width - 5) // 2
            text_y = y + item_height // 2
            self.visual_stack_canvas.create_text(text_x, text_y, text=str(item),
                                               font=("Arial", 10, "bold"), fill=text_color)
            
            # Add position number at bottom
            self.visual_stack_canvas.create_text(text_x, y + item_height + 15,
                                               text=f"[{i}]", font=("Arial", 8),
                                               fill="gray")
        
        # Add stack pointer
        if self.stack:
            arrow_x = start_x + (num_items - 1) * item_width + (item_width - 5) // 2
            arrow_y = canvas_height - item_height - 25
            self.visual_stack_canvas.create_text(arrow_x, arrow_y, text="← TOP",
                                               font=("Arial", 9, "bold"), fill="red")
    
    def shift_action(self):
        """Perform a shift action"""
        if self.input_buffer and not self.parse_complete:
            word = self.input_buffer.pop(0)
            self.stack.append(word)
            self.step_number += 1
            
            action = f"SHIFT '{word}'"
            self.current_action = action
            self.action_history.append(f"Step {self.step_number}: {action}")
            
            self.update_history()
            self.update_display()
    
    def show_reduce_options(self):
        """Show available reduce options"""
        if not self.stack or self.parse_complete:
            return
        
        # Find possible reductions
        possible_reductions = []
        
        # Check all possible suffixes of the stack
        for i in range(len(self.stack)):
            suffix = self.stack[i:]
            suffix_str = " ".join(str(item) for item in suffix)
            
            # Check each grammar rule
            for rule in self.grammar.productions():
                rhs_str = " ".join(str(item) for item in rule.rhs())
                if suffix_str == rhs_str:
                    possible_reductions.append((rule, i))
        
        if not possible_reductions:
            messagebox.showwarning("No Reductions", "No valid reductions available!")
            return
        
        # Create selection dialog
        self.show_reduction_dialog(possible_reductions)
    
    def show_reduction_dialog(self, reductions):
        """Show dialog to select reduction"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Select Reduction")
        dialog.geometry("400x300")
        dialog.transient(self.root)
        dialog.grab_set()
        
        tk.Label(dialog, text="Choose a reduction:", font=("Arial", 12, "bold")).pack(pady=10)
        
        # Create listbox with reductions
        listbox_frame = tk.Frame(dialog)
        listbox_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        listbox = tk.Listbox(listbox_frame, font=("Courier", 10))
        scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=listbox.yview)
        listbox.configure(yscrollcommand=scrollbar.set)
        
        for i, (rule, start_pos) in enumerate(reductions):
            rhs_items = self.stack[start_pos:]
            reduction_text = f"{rule.lhs()} -> {' '.join(str(item) for item in rule.rhs())}"
            listbox.insert(tk.END, f"{i+1}. {reduction_text}")
        
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Buttons
        button_frame = tk.Frame(dialog)
        button_frame.pack(pady=10)
        
        def apply_reduction():
            selection = listbox.curselection()
            if selection:
                rule, start_pos = reductions[selection[0]]
                self.reduce_action(rule, start_pos)
                dialog.destroy()
        
        tk.Button(button_frame, text="Apply", command=apply_reduction, 
                 bg="lightgreen", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=dialog.destroy, 
                 width=10).pack(side=tk.LEFT, padx=5)
        
        # Auto-select first item
        if reductions:
            listbox.select_set(0)
            listbox.focus_set()
    
    def reduce_action(self, rule, start_pos):
        """Perform a reduce action"""
        if self.parse_complete:
            return
        
        # Remove the RHS from stack
        reduced_items = self.stack[start_pos:]
        self.stack = self.stack[:start_pos]
        
        # Add LHS to stack
        self.stack.append(rule.lhs())
        
        self.step_number += 1
        
        rhs_str = " ".join(str(item) for item in reduced_items)
        action = f"REDUCE {rule.lhs()} -> {rhs_str}"
        self.current_action = action
        self.action_history.append(f"Step {self.step_number}: {action}")
        
        self.update_history()
        self.update_display()
    
    def auto_step(self):
        """Automatically determine and perform the next step"""
        if self.parse_complete:
            return
        
        # Simple strategy: prefer reduce over shift when possible
        # Check for possible reductions first
        possible_reductions = []
        
        for i in range(len(self.stack)):
            suffix = self.stack[i:]
            suffix_str = " ".join(str(item) for item in suffix)
            
            for rule in self.grammar.productions():
                rhs_str = " ".join(str(item) for item in rule.rhs())
                if suffix_str == rhs_str:
                    possible_reductions.append((rule, i))
        
        if possible_reductions:
            # Choose the longest reduction (rightmost position)
            rule, start_pos = max(possible_reductions, key=lambda x: x[1])
            self.reduce_action(rule, start_pos)
        elif self.input_buffer:
            # No reductions possible, so shift
            self.shift_action()
        else:
            # No moves possible
            self.update_display()
    
    def reset_parser(self):
        """Reset the parser to initial state"""
        self.reset_parser_state()
        self.history_text.delete(1.0, tk.END)
        self.action_label.config(fg="black")
        self.update_display()
    
    def update_history(self):
        """Update the history display"""
        self.history_text.delete(1.0, tk.END)
        for action in self.action_history:
            self.history_text.insert(tk.END, action + "\n")
        self.history_text.see(tk.END)
    
    def mainloop(self):
        self.root.mainloop()

# Example usage
if __name__ == "__main__":
    # Example grammar - replace with your actual grammar
    grammar = CFG.fromstring("""
        S -> NP VP
        VP -> V NP | V NP PP
        PP -> P NP
        NP -> Det N | Det N PP | 'Mary' | 'Bob'
        Det -> 'the' | 'a'
        N -> 'dog' | 'cat' | 'telescope' | 'park'
        V -> 'saw' | 'walked'
        P -> 'in' | 'with'
    """)
    
    # Example sentence - replace with your actual sentence
    sent = "Mary saw the dog with the telescope".split()
    
    # Create and run the interactive GUI
    app = InteractiveShiftReduceGUI(grammar, sent)
    app.mainloop()
