#include <thread> 
#include <iostream> 
#include <chrono> 
#include "pythreads.h" 
#include <pybind11/embed.h> // everything needed for embedding
#include <filesystem> 

namespace fs = std::filesystem; 


namespace py = pybind11;

void create_task(int index ){
    std::thread subTask([index ]{
            //while(1)
            {
            //    std::this_thread::sleep_for(std::chrono::seconds(1)); 
            std::cout << "begin to execute subtask " << index  << std::endl; 
            PyEnsureGilState ensureGil; 
            //py::print("sub task from python"); // use the Python API
            try {
                    py::module_ mtpy= py::module_::import("mtpi");
                    mtpy.attr("estimate_pi")(100000000); 
                    std::cout << "after to execute subtask" << index  << std::endl; 
                }catch (py::error_already_set &e){
                    std::cout << e.what() << std::endl; 
                }
            }
            }); 


    subTask.detach(); 

}

int main() {
    py::scoped_interpreter guard{}; // start the interpreter and keep it alive

    py::print("Hello, World!"); // use the Python API
    py::module_ sys = py::module_::import("sys"); 

    auto curPath = fs::current_path();
    curPath.make_preferred();
    //auto appendCmd = fmt::format("sys.path.append('{}')", curPath.generic_string() ); 
    auto appendCmd = std::string("sys.path.append('")+curPath.generic_string()+"')"; 
    std::cout << "append command " << appendCmd << std::endl; 
    py::exec(appendCmd.c_str());

    PyEnableThreads enableThreads; 
    create_task(1); 
    create_task(2); 
    while(1){
        std::this_thread::sleep_for(std::chrono::seconds(1)); 
    }
}
