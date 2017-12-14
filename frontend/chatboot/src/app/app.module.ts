import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login-component/login.component';
import { AlertModule } from 'ngx-bootstrap';
import { routing } from './app.routing';
import { FormsModule } from '@angular/forms';
import { HttpModule } from "@angular/http";
import { MenuComponent } from './components/menu-component/menu.component';
import { ProfileComponent } from './components/profile-component/profile.component';
import { ChatroomComponent } from './components/chatroom-component/chatroom.component';
import { RegisterComponent } from './components/register-component/register.component';

@NgModule({
  /*declaram componentele facute*/
  declarations: [
    AppComponent,
    LoginComponent,
    MenuComponent,
    ProfileComponent,
    ChatroomComponent,
    RegisterComponent
  ],
  /* importam anumite dependinte externe daca avem nevoie*/
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AlertModule.forRoot(),
    routing
  ],
  /* aici vom declara serviciile*/
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
