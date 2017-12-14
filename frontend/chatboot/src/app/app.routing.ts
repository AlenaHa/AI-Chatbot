import { ModuleWithProviders } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login-component/login.component';
import { ChatroomComponent } from './components/chatroom-component/chatroom.component';
import { MenuComponent } from './components/menu-component/menu.component';
import { RegisterComponent } from './components/register-component/register.component';
import { ProfileComponent } from './components/profile-component/profile.component';


export const appRoutes: Routes = [
    {path: '', component: LoginComponent},
    {path: 'login', component: LoginComponent},    
    {path: 'chatroom', component: ChatroomComponent},
    {path: 'menu', component: MenuComponent},
    {path: 'register', component: RegisterComponent},
    {path: 'profile', component: ProfileComponent}
    
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);