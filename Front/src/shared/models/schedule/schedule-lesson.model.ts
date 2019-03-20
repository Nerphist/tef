export class ScheduleLessonModel {
  public dayNumber: number;
  public groupName: string;
  public id: number;
  public lessonName: string;
  public lessonNumber: number;
  public lessonRoom: string;
  public lessonType: string;
  public lessonWeek: number;
  public teacher: string;

  constructor(day?) {
    if (day) {
      this.dayNumber = day.day_number;
      this.groupName = day.group_name;
      this.id = day.id;
      this.lessonName = day.lesson_name;
      this.lessonNumber = day.lesson_number;
      this.lessonRoom = day.lesson_room;
      this.lessonType = day.lesson_type;
      this.lessonWeek = day.lesson_week;
      this.teacher = day.teacher;
    }
  }
}
