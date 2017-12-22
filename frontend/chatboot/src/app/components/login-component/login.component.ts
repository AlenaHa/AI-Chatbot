import { Component } from '@angular/core';
import { OnInit } from '@angular/core/src/metadata/lifecycle_hooks';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
/* fiecare componenta pe care o facem trebuie sa aibe o structura de genu
   si componenta va fi inregistrata in app.module.ts*/
export class LoginComponent implements OnInit {
  constructor(private router: Router) { }
  
  redirectOnRegister(){
    this.router.navigate(['/register']);
  }

  redirectOnChat() {
    this.router.navigate(['/chatroom']);
  }

  ngOnInit() {
    
  }
}
