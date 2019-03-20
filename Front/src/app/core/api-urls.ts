export class ApiUrls {
  private static readonly apiRoot: string = 'http://93.188.34.235:8088/';

  public static getSheduleUrl(): string {
    return `${this.apiRoot}time-schedule`;
  }
}
