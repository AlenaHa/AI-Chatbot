import { Component, OnInit } from '@angular/core';
import { User } from '../../models/user.model';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  private user: User;
  private editIsDisabled: boolean;
  
  ngOnInit() {
    this.user = new User('Prenume','Nume','UMF Iasi','3');
    this.editIsDisabled = false;
  }

  private deleteProfileInformation(): void{
    this.user.lastname = "";
    this.user.faculty = "";
    this.user.name = "";
    this.user.yearFaculty = "";
  }

  private editProfileInformation(): void{
    this.editIsDisabled = true;
  }

  private saveInformation():void{
    this.editIsDisabled = false;
  }

}
