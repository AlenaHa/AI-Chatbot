import { Component, OnInit } from '@angular/core';
import * as myGlobals  from 'globals';
import { ActivatedRoute, Router, NavigationEnd } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  isLoggedIn: boolean;
  showSideBar: boolean;
  showNav: boolean;

  constructor(
    private router:Router){
    this.showNav = true;
    this.showSideBar = true;
  }
    
  ngOnInit(){
      this.router.events.subscribe((e) => {
      if (e instanceof NavigationEnd) {
        let urlSlice = e.url.toString().substr(0,10);
        if(urlSlice.indexOf('login')!==-1){
         this.isLoggedIn= true;
      
        }
        else{
          this.isLoggedIn= false;      }
      }
      });
  }
}
