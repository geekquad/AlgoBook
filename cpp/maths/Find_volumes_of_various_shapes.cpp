#include <bits/stdc++.h>
#include <math.h>
using namespace std;


void volume_of_cube(float side){
    float cube_volume = side*side*side;
    cout << "The volume of cube = " << cube_volume <<endl;
}

void volume_of_cuboid(float side1, float side2, float side3){
    float cuboid_volume = side1*side2*side3;
    cout << "The volume of cuboid = " << cuboid_volume << endl;
}

void volume_of_cone(float height , float radius){
    float cone_volume = (M_PI*radius*radius*height)/3.0;
    cout << "The volume of cone = " << cone_volume <<endl;
}

void volume_of_rt_circular_cone(float height , float radius){
    float rt_cone_volume = (M_PI*radius*radius*height)/3.0;
    cout << "The volume of right circular cone = " << rt_cone_volume << endl;
}

void volume_of_prism(float base_area , float height){
    float prism_volume = base_area*height;
    cout << "The volume of prism = " << prism_volume << endl;
}

void volume_of_pyramid(float base_length ,float base_width , float height){
    float pyramid_volume = (base_length*base_width*height)/3.0;
    cout << "The volume of pyramid = " << pyramid_volume << endl;
}

void volume_of_sphere(float radius){
    float sphere_volume = (M_PI*radius*radius*radius*4)/3.0;
    cout << "The volume of sphere = " << sphere_volume;
}

void volume_of_circular_cylinder(float height , float radius){
    float circular_cylinder = M_PI*radius*radius*height;
    cout << "The volume of circular cylinder= " << circular_cylinder;
}

int main(){
    float side,side1,side2,side3,height,radius,area,blength,width;
    cout << "Enter your option for finding volume of desired shape" << endl;
    cout << "Enter 1 for Cube , 2 for Cuboid , 3 for Cone , 4 for Right circular cone" << endl;
    cout << "Enter 5 for Prism , 6 for Pyramid , 7 for Sphere , 8 for Circular Cylinder" << endl;
    cout << "Enter your choice" << endl;
    int choice;
    cin >> choice ;
    switch(choice){
        case 1:
        cout << "Enter side of cube" << endl;
        cin >> side ;
        volume_of_cube(side);
        break;

        case 2:
        cout << "Enter side of cuboid" << endl;
        cin >> side1 >> side2 >> side3 ;
        volume_of_cuboid(side1 , side2 ,side3);
        break;

        case 3:
        cout << "Enter height and radius of cone" << endl;
        cin >> height >> radius ;
        volume_of_cone(height , radius);
        break;

        case 4:
        cout << "Enter height and radius of Right circular cone" << endl;
        cin >> height >> radius ;
        volume_of_rt_circular_cone(height , radius);
        break;

        case 5:
        cout << "Enter height and base area of Prism" << endl;
        cin >> height >> area ;
        volume_of_prism(area, height);
        break;

        case 6:
        cout << "Enter base length ,width , height of Pyramid" << endl;
        cin >> blength >> width >> height >> area ;
        volume_of_pyramid(blength , width , height);
        break;

        case 7:
        cout << "Enter radius of sphere" << endl;
        cin >> radius ;
        volume_of_sphere( radius);
        break;

        case 8:
        cout << "Enter height and radius of circular cylinder" << endl;
        cin >> height >> radius ;
        volume_of_circular_cylinder(height , radius);
        break;

        default:
        cout << "Wrong Choice" << endl;
    }

    return 0;
}
