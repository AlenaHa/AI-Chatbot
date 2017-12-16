/** exemplu de model */

export class User{
    name: string;
    lastname: string;
    faculty: string;
    yearFaculty: number;
    password: string;

    public constructor(_name: string, _lastname: string, _faculty: string, _yearFaculty: number){
        this.name = _name;
        this.lastname = _lastname;
        this.faculty = _faculty;
        this.yearFaculty = _yearFaculty;
    }
}
