import { ModuleWithProviders } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login-component/login.component';

export const appRoutes: Routes = [
    {path: '', component: LoginComponent}
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);