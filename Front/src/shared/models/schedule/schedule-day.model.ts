import { ScheduleLessonModel } from './schedule-lesson.model';

export class ScheduleDayModel {
  public lessons: ScheduleLessonModel[];

  constructor(lessons?) {
    this.lessons = [];
    let index = 0;
    for (let i = 0; i < 5; i++) {
      if (lessons[index] && lessons[index].lesson_number === i + 1) {
          this.lessons.push(new ScheduleLessonModel(lessons[index]));
          index++;
      } else {
          this.lessons.push(new ScheduleLessonModel());
      }
    }
  }
}
