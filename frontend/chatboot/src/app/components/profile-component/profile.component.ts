import { Component, OnInit } from '@angular/core';
import { User } from '../../models/user.model';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  private user: User;

  ngOnInit() {
    this.user = new User('Ecaterina','Manolache','UMF Iasi',3);
    console.log(this.user);
  }

}
