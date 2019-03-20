import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filter',
  pure: false
})
export class FilterPipe implements PipeTransform {

  public transform<T>(value: T[], args: string): T[] {
    if (!value || !args) {
      return [];
    }


    return value
      .filter(item => Array(item).toString().toUpperCase().includes(args.toUpperCase())
      );
  }

}
