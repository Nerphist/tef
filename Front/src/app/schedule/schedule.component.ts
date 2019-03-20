import { Component, OnInit } from '@angular/core';

import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { ScheduleModel } from '../../shared/models/schedule/schedule.model';

import { ScheduleService } from '../core/shedule/schedule.service';

@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.scss']
})
export class ScheduleComponent implements OnInit {

  public groups$: Observable<string[]>;
  public schedule$: Observable<ScheduleModel>;

  public input1: string;

  public isScheduleChosen = false;
  public chosenGroup: string;

  public lessonNumber: string[];

  constructor(
    private scheduleService: ScheduleService
  ) { }

  public ngOnInit(): void {
    this.input1 = '';

    this.lessonNumber = [
      'I', 'II', 'III', 'IV', 'V'
    ];

    this.groups$ = this.scheduleService.getGroups().pipe(
        map((groups) => Object.values(groups))
    );
  }

  public choseGroup(group: string): void {
    this.chosenGroup = group;

    this.schedule$ = this.scheduleService.getSchedule(this.chosenGroup)
      .pipe(
        map((x) => new ScheduleModel(x['1 week'], x['2 week']))
      );

    this.isScheduleChosen = true;
  }

  public exit(): void {
    this.input1 = '';

    this.isScheduleChosen = false;
  }
}
