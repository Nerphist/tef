import { ScheduleDayModel } from './schedule-day.model';

export class ScheduleModel {
  public week1: ScheduleDayModel[];
  public week2: ScheduleDayModel[];

  constructor(week1, week2) {
    this.week1 = [];
    this.week2 = [];
    Object.values(week1).forEach((day, index) => {
      // @ts-ignore
      if (day.length !== 0) {
        this.week1[index] = new ScheduleDayModel(day);
      }
    });
    Object.values(week2).forEach((day, index) => {
      // @ts-ignore
      if (day.length !== 0) {
        this.week2[index] = new ScheduleDayModel(day);
      }
    });
  }
}
