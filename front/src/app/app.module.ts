import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { GustafDbService } from './gustaf-db.service';
import { ShowListComponent } from './show-list/show-list.component';
import { HttpModule } from '@angular/http';

@NgModule({
  declarations: [
    AppComponent,
    ShowListComponent
  ],
  imports: [
    BrowserModule,
    HttpModule
  ],
  providers: [GustafDbService],
  bootstrap: [AppComponent]
})
export class AppModule { }
