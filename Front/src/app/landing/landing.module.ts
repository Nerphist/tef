import { NgModule } from '@angular/core';
import { LandingComponent } from './landing.component';
import { BrowserModule, HAMMER_GESTURE_CONFIG, HammerGestureConfig } from '@angular/platform-browser';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { HttpClient } from '@angular/common/http';
import { TranslateLoader, TranslateModule } from '@ngx-translate/core';
import { DepartmentDescriptionComponent } from '../department-description/department-description.component';

import 'hammerjs';
import { RouterModule, Routes } from '@angular/router';
import { TranslateHttpLoader } from '@ngx-translate/http-loader';
import { PerfectScrollbarModule } from 'ngx-perfect-scrollbar';
import { ScheduleComponent } from '../schedule/schedule.component';

const appRoutes: Routes = [
  { path: 'schedule', component: ScheduleComponent},
  { path: '**', component: LandingComponent }
];

export class MyHammerConfig extends HammerGestureConfig {
  overrides = {
    pinch: {enable: false},
    rotate: {enable: false}
  } as any;
}

@NgModule({
  declarations: [
    LandingComponent,
    DepartmentDescriptionComponent
  ],
  imports: [
    BrowserModule,
    NgbModule,
    PerfectScrollbarModule,
    TranslateModule.forRoot({
      loader: {
        provide: TranslateLoader,
        useFactory: HttpLoaderFactory,
        deps: [HttpClient]
      }
    })
  ],
  exports: [
    LandingComponent,
    DepartmentDescriptionComponent
  ],
  providers: [
    {
      provide: HAMMER_GESTURE_CONFIG,
      useClass: MyHammerConfig
    }
  ],
  entryComponents: [ DepartmentDescriptionComponent ],
})
export class LandingModule { }

// required for AOT compilation
export function HttpLoaderFactory(http: HttpClient) {
  return new TranslateHttpLoader(http);
}
