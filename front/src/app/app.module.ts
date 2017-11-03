import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { GustafDbService } from './gustaf-db.service';
import { ShowListComponent } from './show-list/show-list.component';
import { HttpModule } from '@angular/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { EpisodeListComponent } from './episode-list/episode-list.component';

@NgModule({
  declarations: [
    AppComponent,
    ShowListComponent,
    EpisodeListComponent,
  ],
  imports: [
    BrowserModule,
    HttpModule,
    NgbModule.forRoot(),
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [GustafDbService],
  bootstrap: [AppComponent]
})
export class AppModule { }
