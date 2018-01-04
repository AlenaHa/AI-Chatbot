import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent {
  constructor(private router:Router){}

  openNav():void {
  document.getElementById("mySidenav").style.width = "250px";
  }

 closeNav():void {
  document.getElementById("mySidenav").style.width = "0";
  }

route(event): void{
  if(event == 1){
    this.router.navigate(["/chatroom"]); 
  }else if(event == 2){
    this.router.navigate(['/profile']); 
  }else if( event == 3){
    this.router.navigate(['/login']); 
  }
  this.closeNav();
  }
}
