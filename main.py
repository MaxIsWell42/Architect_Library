from absl import app
from absl import flags
from os import path

FLAGS = flags.FLAGS

flags.DEFINE_bool('r', True, 'Read a job')
flags.DEFINE_string('w', 'Name, Job Number, Notes', 'Add a new entry')
flags.DEFINE_string('name', None, 'Job Name')
flags.DEFINE_integer('number', None, 'Job Number')


def main(argv):
    if path.isfile('theLibrary.txt') != True:
        open('theLibrary.txt')
        
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
                        
    if FLAGS.w == True:
        with open('theLibrary.txt', 'w') as file:
            for line in file:
                if line.isspace():
                    file.write(FLAGS.w)
                        
                    

if __name__ == "__main__":
    app.run(main)