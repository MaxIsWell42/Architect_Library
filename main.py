from absl import app
from absl import flags
from os import path

FLAGS = flags.FLAGS

flags.DEFINE_bool('r', True, 'Read a job')
flags.DEFINE_bool('w', False, 'Add a new entry')
flags.DEFINE_string('name', None, 'Job Name')
flags.DEFINE_integer('number', None, 'Job Number')


def main(argv):
    if path.isfile('theLibrary.txt') != True:
        file = open('theLibrary.txt', 'x')
        
    if FLAGS.r == True:
        with open('theLibrary.txt', 'r') as file:
            if FLAGS.name:
                for line in file:
                    if FLAGS.name.lower() in line.lower():
                        print(line)
                        
            elif FLAGS.number:
                for line in file:
                    if FLAGS.number in line:
                        print(line)
            file.close()
                        

    if FLAGS.w:
        with open('theLibrary.txt', 'a') as file:
            name = input("Job Name: ")
            number = input("Job Number: ")
            notes = input("Job Info: ")
            job = str([name, number, notes])
            file.write("\n{}".format(job))
            file.close()
                        
                    

if __name__ == "__main__":
    app.run(main)