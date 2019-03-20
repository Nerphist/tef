import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { ApiUrls } from '../api-urls';

@Injectable({
  providedIn: 'root'
})
export class ScheduleService {

  constructor(
    private http: HttpClient
  ) { }

  public getSchedule(group: string) {
    return this.http.get(ApiUrls.getSheduleUrl() + '/' + group + '/');
  }

  public getGroups() {
    return this.http.get(ApiUrls.getSheduleUrl() + '/groups/');
  }
}
