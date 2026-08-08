from experta import *


class StudentFacts(Fact):
    pass


class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")

    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Biology'))
    def bioinformatics(self):
        print("Suggested Career Path: Bioinformatics")

    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Chemistry'))
    def chemical(self):
        print("Suggested Career Path: Chemical Engineering")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")

    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")

    @Rule(StudentFacts(likes='Physics'), StudentFacts(likes='Programming'))
    def quantum(self):
        print("Suggested Career Path: Quantum Computing")

    @Rule(StudentFacts(likes='Physics'), StudentFacts(likes='Biology'))
    def biophysics(self):
        print("Suggested Career Path: Biophysics")

    # NOTE: originally named 'chemical' (duplicate of the Maths+Chemistry rule above),
    # and had no body at all -> IndentationError. Renamed to 'physics_chemistry' and
    # given a placeholder message -- change the text to whatever you intended.
    @Rule(StudentFacts(likes='Physics'), StudentFacts(likes='Chemistry'))
    def physics_chemistry(self):
        print("Suggested Career Path: Materials Science and Engineering")

    @Rule(StudentFacts(likes='Physics'), StudentFacts(likes='Circuits'))
    def ee(self):
        print("Suggested Career Path: Electrical and Electronics Engineering")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Chemistry'))
    def cc(self):
        print("Suggested Career Path: Computational Chemistry")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Circuits'))
    def ese(self):
        print("Suggested Career Path: Embedded Systems Engineering")

    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")

    # NOTE: originally named 'bioinformatics' (duplicate of the Maths+Biology rule above),
    # and had no body at all -> IndentationError. Renamed to 'computational_biology' and
    # given a placeholder message -- change the text to whatever you intended.
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Programming'))
    def computational_biology(self):
        print("Suggested Career Path: Computational Biology")

    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Circuits'))
    def be(self):
        print("Suggested Career Path: Biomedical Engineering")

    @Rule(StudentFacts(likes='Chemistry'), StudentFacts(likes='Circuits'))
    def semiconductor(self):
        print("Suggested Career Path: Semiconductor Engineering")


def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("\nWelcome to the Career Path Expert System!")
    interests = input("\nEnter your interests separated by commas : \nOptions : (Any Two)\n\n1.Maths \t2.Physics\t3.Programming\n4.Biology\t5.Chemistry\t6.Circuits\n\nSelect from options above: ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()


if __name__ == "__main__":
    main()
