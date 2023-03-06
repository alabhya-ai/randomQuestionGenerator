import tkinter as tk
import generate

class QuestionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Random Question Generator - by Alabhya")

        self.isChapterWise = False
        self.chapChose = ""

        # Subject Selection
        self.subjectLabel = tk.Label(master, text="Subject")
        self.subjectLabel.pack()

        self.subjectVar = tk.StringVar()
        self.subjectVar.set("Mathematics")  # default value

        self.subjectOption = tk.OptionMenu(master, self.subjectVar, "Physics", "ComputerScience", "Mathematics", "Chemistry")
        self.subjectOption.pack()

        self.practiceTypeLabel = tk.Label(master, text="What type of practice do you want to do?")
        self.practiceTypeLabel.pack()

        # Practice type selection
        self.practiceTypeFrame = tk.Frame(master)
        self.practiceTypeFrame.pack()

        self.randomButton = tk.Button(self.practiceTypeFrame, text="Random Questions", command=self.randomPractice)
        self.randomButton.pack(side=tk.LEFT)

        self.chapterButton = tk.Button(self.practiceTypeFrame, text="Chapter-wise practise", command=self.chapterPractice)
        self.chapterButton.pack(side=tk.RIGHT)

        # Back button
        self.backButton = tk.Button(master, text="Back", command=self.master.destroy)
        self.backButton.pack(side=tk.BOTTOM)

    def randomPractice(self):
        self.isChapterWise = False
        self.openQuestionPopup()

    def chapterPractice(self):
        self.isChapterWise = True

        # Chapter selection
        self.chapterWindow = tk.Toplevel(self.master)
        self.chapterWindow.title("Chapter Selection")

        self.chapterLabel = tk.Label(self.chapterWindow, text="Chapter")
        self.chapterLabel.pack()

        self.chapterVar = tk.StringVar()
        self.chapterOption = tk.OptionMenu(self.chapterWindow, self.chapterVar, *generate.subList(self.subjectVar.get()))
        self.chapterOption.pack()

        self.generateButton = tk.Button(self.chapterWindow, text="Generate", command=self.openQuestionPopup)
        self.generateButton.pack(side=tk.BOTTOM)

        # Back button
        self.backButton = tk.Button(self.chapterWindow, text="Back", command=self.chapterWindow.destroy)
        self.backButton.pack(side=tk.LEFT)

    def openQuestionPopup(self):
        if hasattr(self, "questionWindow"): # close previous questionWindows
            self.questionWindow.destroy()

        if self.isChapterWise:
            self.chapChose = self.chapterVar.get()
            questionStr = generate.generateQuestion(1, self.chapChose[(self.chapChose.index(".") + 1):(self.chapChose.index("-"))].strip())
        else:
            questionStr = generate.generateQuestion(0, "")

        # Question popup
        self.questionWindow = tk.Toplevel(self.master)
        self.questionWindow.title("Question")

        self.questionLabel = tk.Label(self.questionWindow, text=questionStr, font=("Arial", 16))
        self.questionLabel.pack()


        # Make window resizable
        self.questionWindow.resizable(True, True)

        # Increase size of the window
        width, height = self.questionWindow.winfo_reqwidth(), self.questionWindow.winfo_reqheight()
        self.questionWindow.geometry(f"{int(width*5)}x{int(height*2)}")

        # Next Button
        self.nextButton = tk.Button(self.questionWindow, text="Next", command=self.openQuestionPopup)
        self.nextButton.pack(side=tk.BOTTOM)

root = tk.Tk()
questionGUI = QuestionGUI(root)
root.mainloop()
