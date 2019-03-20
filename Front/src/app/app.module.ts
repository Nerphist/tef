import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import {TranslateHttpLoader} from '@ngx-translate/http-loader';
import {HttpClient, HttpClientModule} from '@angular/common/http';

import { AppComponent } from './app.component';
import { LandingComponent } from './landing/landing.component';
import { RouterModule, Routes } from '@angular/router';

import { HeaderModule } from './header/header.module';
import { LandingModule } from './landing/landing.module';
import { ScheduleComponent } from './schedule/schedule.component';
import { FilterPipe } from './pipes/filter.pipe';
import { FormsModule } from '@angular/forms';

const appRoutes: Routes = [
  { path: 'schedule', component: ScheduleComponent},
  { path: '**', component: LandingComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    ScheduleComponent,
    FilterPipe,
  ],
  imports: [
    HeaderModule,
    LandingModule,
    CommonModule,
    FormsModule,
    RouterModule.forRoot(
      appRoutes
    ),
    HttpClientModule,
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }

// required for AOT compilation
export function HttpLoaderFactory(http: HttpClient) {
  return new TranslateHttpLoader(http);
}
