import { Component, HostListener, OnInit } from '@angular/core';

import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent implements OnInit {

  constructor(
    private translate: TranslateService
  ) {}

  public isMenuOpen = false;

  @HostListener('touchmove', ) onHover() {
    event.preventDefault();
  }

  public ngOnInit(): void {
    this.translate.setDefaultLang('ukr');
  }

  public openMenu(): void {
    this.isMenuOpen = !this.isMenuOpen;
    console.log(this.isMenuOpen);
  }


  public changeLanguage(language: string): void {
    this.translate.setDefaultLang(language);
  }
}
