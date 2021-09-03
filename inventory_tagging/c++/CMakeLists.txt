cmake_minimum_required(VERSION 3.19)
project(inv_tagging)

set(CMAKE_CXX_STANDARD 14)

include_directories(inv_tagging)

add_executable(clion_projects
        inv_tagging/DAO.cpp
        inv_tagging/DAO.h
        inv_tagging/DeptContact.cpp
        inv_tagging/DeptContact.h
        inv_tagging/driver.cpp
        inv_tagging/inv_tag.cpp
        inv_tagging/inv_tag.h
        inv_tagging/PurchaseDocument.cpp
        inv_tagging/PurchaseDocument.h
        )