export class User{
    name: string;
    lastname: string;
    faculty: string;
    yearFaculty: string;
    password: string;

    public constructor(_name: string, _lastname: string, _faculty: string, _yearFaculty: string){
        this.name = _name;
        this.lastname = _lastname;
        this.faculty = _faculty;
        this.yearFaculty = _yearFaculty;
    }
}
