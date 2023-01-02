#include <iostream>
#include <cstdlib>

int main() {
  std::string sourceFolder = "\"C:\\Users\\light-bringer\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data\"";
  std::string destination = "\"C:\\Users\\light-bringer\\Desktop\\ChromeData\"";

  std::string command = "xcopy /Y " + sourceFolder + " " + destination;
  std::cout << command;
  system(command.c_str());
  std::cout << "Done!" << std::endl;

  return 0;
}
