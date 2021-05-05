<template>
  <q-layout view="lhr lpr lfr">
    <!--// Left Drawer Starts-->
    <q-drawer v-model="leftDrawerOpen" show-if-above bordered :content-style="{ backgroundColor: 'rgba(199, 235, 235, 0.5)' }">
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeatureMedBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxmedoptions" :series="selectedFeatureMedBarBox" />
              </td>
            </tr>
          </div>
        </table>
      </q-card>
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeatureAvgBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxavgoptions" :series="selectedFeatureAvgBarBox" />
              </td>
            </tr>
          </div>
        </table>
      </q-card>
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeatureMinBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxminoptions" :series="selectedFeatureMinBarBox" />
              </td>
            </tr>
          </div>
        </table>
      </q-card>
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeatureMaxBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxmaxoptions" :series="selectedFeatureMaxBarBox" />
              </td>
            </tr>
          </div>
        </table>
      </q-card>
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeatureStdBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxstdoptions" :series="selectedFeatureStdBarBox" />
              </td>
            </tr>
          </div>
        </table>
      </q-card>
    </q-drawer>
    <!--// Left Drawer Ends -->

    <!--// right side drawer Starts -->
    <q-drawer side="right" v-model="rightDrawerOpen" show-if-above bordered content-class="teal bg-teal-1">
      <q-list bordered class="rounded-borders">
        <!-- // baselayers -->
        <q-expansion-item default-opened expand-separator icon="list" label="Base Layers">
          <div class="q-pa-md" style="min-width: 200px">
            <q-list link>
              <!--//
                Rendering a <label> tag (notice tag="label")
                so QRadios will respond to clicks on QItems to
                change Toggle state.
              -->
              <q-item tag="label" v-ripple>
                <q-item-section avatar>
                  <q-radio v-on:input="showBaseLayer" val="osm" v-model="baselayer" color="teal" />
                </q-item-section>
                <q-item-section>
                  <q-item-label>OpenStreetMap</q-item-label>
                </q-item-section>
              </q-item>

              <q-item tag="label" v-ripple>
                <q-item-section avatar>
                  <q-radio v-on:input="showBaseLayer" val="mapbox" v-model="baselayer" color="teal" />
                </q-item-section>
                <q-item-section>
                  <q-item-label>MapBox Satellite</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </div>
        </q-expansion-item>
        <!-- // baselayers -->

        <!-- // NC wellwise layers -->
        <q-expansion-item default-opened expand-separator icon="list" label="NC Well Data Layers, by Census Tracts">
          <div class="q-pa-md q-gutter-y-sm column">
            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_arsenic_med" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Arsenic Median</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_arsenic_mean" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Arsenic Mean</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_cadmium_med" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Cadmium Median</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_lead_med" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Lead Median</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="ncwellwise_mng_med" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Manganese Median</q-item-label>
              </q-item-section>
            </q-item>
          </div>
        </q-expansion-item>
        <!-- // NC wellwise layers -->

        <!-- // LTDB Census layers -->
        <q-expansion-item expand-separator icon="list" label="Socioeconomic Layers, by Census Tracts">
          <div class="q-pa-md q-gutter-y-sm column">
            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="pnhwht12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Non-Hispanic White</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="pnhblk12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Non-Hispanic Black</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="phisp12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Hispanic</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="pasian12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Asian</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="pntv12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Percent Native American</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="hincw12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Median HH income, white</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="hincb12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Median HH income, black</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="hinch12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Median HH income, hispanic</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="hinca12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Median HH income, asian</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="pwpov12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>% in poverty, white</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="pbpov12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>% in poverty, black</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="phpov12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>% in poverty, hispanic</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="papov12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>% in poverty, asian</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="pnapov12" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>% in poverty, native American</q-item-label>
              </q-item-section>
            </q-item>
          </div>
        </q-expansion-item>
        <!-- // LTDB Census layers -->

        <!-- // EJScreen layers -->
        <q-expansion-item expand-separator icon="list" label="Environmental Justice Layers, by Census Block Group">
          <div class="q-pa-md q-gutter-y-sm column">
            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_ldpnt_2" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for % pre-1960 housing (lead paint indicator)</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_dslpm_2" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Diesel particulate matter level in air</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_cancr_2" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Air toxics cancer risk</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_resp_2" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Air toxics respiratory hazard index</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_ptraf_2" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Traffic proximity and volume</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_pwdis_2" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Indicator for major direct dischargers to water</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_pnpl_2" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Proximity to National Priorities List (NPL) sites</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_prmp_2" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Proximity to Risk Management Plan (RMP) facilities</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_ptsdf_2" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Proximity to Treatment Storage and Disposal (TSDF) facilities</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_ozone_2" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for Ozone level in air</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="d_pm25_2" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>EJ Index for PM2.5 level in air</q-item-label>
              </q-item-section>
            </q-item>
          </div>
        </q-expansion-item>
        <!-- // EJScreen layers -->

        <!-- // Health layers -->
        <q-expansion-item expand-separator icon="list" label="Health Layers, by Zip Code">
          <div class="q-pa-md q-gutter-y-sm column">
            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="cases" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Covid-19 Total Cases</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="cases_per_10000_res" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Covid-19 Cases Per 10,000 Residents</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="cases_per_100000_res" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Covid-19 Cases Per 100,000 Residents-</q-item-label>
              </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
              <q-item-section avatar>
                <q-radio v-on:input="showMapPanelRadioLayer" val="deaths" v-model="currentlayer" color="teal" />
              </q-item-section>
              <q-item-section>
                <q-item-label>Covid-19 Deaths</q-item-label>
              </q-item-section>
            </q-item>
           </div>
        </q-expansion-item>
        <!-- // Health layers -->

        <!-- // Ancillary layers -->
        <q-expansion-item expand-separator icon="list" label="Ancillary Layers">
          <div class="q-pa-md q-gutter-y-sm column">
            <q-toggle
              :label="`North Carolina Counties ${ ncCountiesModel }`"
              :key="layers[4].id"
              v-on:input="showMapPanelToggleLayer(layers)"
              :class="{ 'is-active': layers[4].visible }"
              color="teal"
              false-value="Not Selected"
              true-value="Selected"
              v-model="ncCountiesModel"
            />
           </div>
        </q-expansion-item>
        <!-- // Ancilary layers -->

        <!-- // state -->
        <q-expansion-item expand-separator icon="list" label="State">
          <q-markup-table class="table is-fullwidth bg-teal-1" dense>
            <tr>
              <th class="text-left">Map center</th>
              <td class="text-left" style="font-size:10px">{{ center[0]}}, {{ center[1] }}</td>
            </tr>
            <tr>
              <th class="text-left">Map zoom</th>
              <td class="text-left" style="font-size:10px">{{ zoom }}</td>
            </tr>
            <tr>
              <th class="text-left">Map rotation</th>
              <td class="text-left" style="font-size:10px">{{ rotation }}</td>
            </tr>
            <tr>
              <th class="text-left">Event coordinate</th>
              <td class="text-left" style="font-size:10px">{{ eventCoordinate[0] }}, {{ eventCoordinate[1] }}</td>
            </tr>
            <tr>
              <th class="text-left">Device coordinate</th>
              <td class="text-left" style="font-size:10px">{{ deviceCoordinate[0] }}, {{ deviceCoordinate[1] }}</td>
            </tr>
            <tr>
              <th class="text-left">Coordinate accuracy</th>
              <td class="text-left" style="font-size:10px">{{ coordinateAccuracy }} meters</td>
            </tr>
            <tr>
              <th class="text-left">Selected features</th>
              <td class="text-left" style="font-size:10px">{{ pid }}</td>
            </tr>
          </q-markup-table>
        </q-expansion-item>
        <!-- // state -->

        <!-- // legend -->
        <q-expansion-item expand-separator icon="list" label="Legend">
          <q-markup-table class="bg-teal-1">
            <tr>
              <td id="nested">
                <tr>
                  <q-expansion-item expand-separator icon="list" label="Arsenic Maximum (ppb)">
                    <q-markup-table class="bg-teal-1">
                      <tr>
                        <td id="nested">
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                          <td>Fill -999.99</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu1"></span></td>
                            <td>&gt; 5</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu2"></span></td>
                            <td>&ge; 5 &amp; &lt; 9</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu3"></span></td>
                            <td>&ge; 9 &amp; &lt; 12</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu4"></span></td>
                            <td>&ge; 12 &amp; &lt; 16</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu5"></span></td>
                            <td>&ge; 16</td>
                          </tr>
                        </td>
                      </tr>
                    </q-markup-table>
                  </q-expansion-item>
                </tr>
                <tr>
                  <q-expansion-item expand-separator icon="list" label="Cadmium Maximum (ppb)">
                    <q-markup-table class="bg-teal-1">
                      <tr>
                        <td id="nested">
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                          <td>Fill -999.99</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu1"></span></td>
                            <td>&gt; 5</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu2"></span></td>
                            <td>&ge; 5 &amp; &lt; 22</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu3"></span></td>
                            <td>&ge; 22 &amp; &lt; 33</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu4"></span></td>
                            <td>&ge; 33 &amp; &lt; 44</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu5"></span></td>
                            <td>&ge; 44 &amp; &lt; 55</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="cdsqu6"></span></td>
                            <td>&ge; 55</td>
                          </tr>
                        </td>
                      </tr>
                    </q-markup-table>
                  </q-expansion-item>
                </tr>
                <tr>
                  <q-expansion-item expand-separator icon="list" label="Lead Maximum (ppb)">
                    <q-markup-table class="bg-teal-1">
                      <tr>
                        <td id="nested">
                          <tr>
                            <td style="padding:5px"><span class="pbsqufill"></span></td>
                          <td>Fill -999.99</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu1"></span></td>
                            <td>&gt; 11</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu2"></span></td>
                            <td>&ge; 11 &amp; &lt; 30</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu3"></span></td>
                            <td>&ge; 30 &amp; &lt; 50</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu4"></span></td>
                            <td>&ge; 50 &amp; &lt; 80</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu5"></span></td>
                            <td>&ge; 80 &amp; &lt; 100</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="pbsqu6"></span></td>
                            <td>&ge; 100</td>
                          </tr>
                        </td>
                      </tr>
                    </q-markup-table>
                  </q-expansion-item>
                </tr>
                <tr>
                  <q-expansion-item expand-separator icon="list" label="Maganese Maximum (ppb)">
                    <q-markup-table class="bg-teal-1">
                      <tr>
                        <td id="nested">
                          <tr>
                            <td style="padding:5px"><span class="squfill"></span></td>
                          <td>Fill -999.99</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu1"></span></td>
                            <td>&gt; 2800</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu2"></span></td>
                            <td>&ge; 2800 &amp; &lt; 5800</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu3"></span></td>
                            <td>&ge; 5800 &amp; &lt; 10800</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu4"></span></td>
                            <td>&ge; 10800 &amp; &lt; 20800</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu5"></span></td>
                            <td>&ge; 20800 &amp; &lt; 40800</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="mnsqu6"></span></td>
                            <td>&ge; 40800</td>
                          </tr>
                        </td>
                      </tr>
                    </q-markup-table>
                  </q-expansion-item>
                </tr>
                <tr>
                  <q-markup-table class="bg-teal-1">
                    <tr>
                      <td><img :src=" 'statics/marker.png' " height="50" width="50"></td>
                      <td>Current Location</td>
                    </tr>
                  </q-markup-table>
                </tr>
              </td>
            </tr>
          </q-markup-table>
        </q-expansion-item>
        <!-- // legend -->

      </q-list>
    </q-drawer>
    <!--// left side drawer Ends -->

    <!--// app map -->
    <vl-map v-if="mapVisible" class="map" ref="map" :load-tiles-while-animating="true" :load-tiles-while-interacting="true"
      @singleclick="onMapClick" data-projection="EPSG:4326" @mounted="onMapMounted" :controls="false" style="height:1200px">
       <!--// map view aka ol.View -->
      <vl-view ref="view" :center.sync="center" :zoom.sync="zoom" :rotation.sync="rotation"></vl-view>

      <!--// click interactions -->
      <vl-interaction-select ref="selectInteraction" :layers="layer => !(layer instanceof VectorTile)" :features.sync="selectedFeature">
      <!-- vl-interaction-select ref="selectInteraction" :filter="(feature, layer) => feature instanceof Feature" :features.sync="selectedFeature" -->
      <!-- vl-interaction-select ref="selectInteraction" :features.sync="selectedFeature" -->
        <template slot-scope="select">
          <!--// select styles -->
          <vl-style-box>
            <vl-style-stroke color="#33201e" :width="7"></vl-style-stroke>
            <vl-style-fill :color="[254, 178, 76, 0.7]"></vl-style-fill>
            <vl-style-circle :radius="5">
              <vl-style-stroke color="#9e493e" :width="7"></vl-style-stroke>
              <vl-style-fill :color="[254, 178, 76, 0.7]"></vl-style-fill>
            </vl-style-circle>
          </vl-style-box>
          <vl-style-box :z-index="1">
            <vl-style-stroke color="#d43f45" :width="2"></vl-style-stroke>
            <vl-style-circle :radius="5">
              <vl-style-stroke color="#d43f45" :width="2"></vl-style-stroke>
            </vl-style-circle>
          </vl-style-box>
          <!--// select styles -->

          <!--// selected feature popup -->
          <vl-overlay class="feature-popup" v-for="feature in select.features" :key="feature.id" :id="feature.id"
            :position="pointOnSurface(feature.geometry)" :auto-pan="true" :auto-pan-animation="{ duration: 300 }">
            <q-card class="feature-popup">
              <q-card-section>
                <q-banner inline-actions class="text-black bg-white">
                  <div class="text-h6">
                    Feature GeoID {{ feature.properties['geoid10'] }}
                  </div>
                  <template v-slot:action>
                    <q-btn flat round dense icon="close" @click="selectedFeature = selectedFeature.filter(f => f.id !== feature.id)" />
                  </template>
                </q-banner>
                <table class="table is-fullwidth">
                  <div v-if="Object.keys(selectedFeatureMaxBarBox).length > 0">
                  <tr>
                    <td>
                      <!-- apexchart width="400" type="radialBar" :options="apxavgoptions" :series="selectedFeatureAvgBarBox" / -->
                      <!-- apexchart type="radialBar" :options="apxavgoptions" :series="selectedFeatureAvgBarBox" / -->
                    </td>
                  </tr>
                  </div>
                </table>
              </q-card-section>
            </q-card>
          </vl-overlay>
          <!--// selected feature popup -->
        </template>
      </vl-interaction-select>
      <!--// click interactions -->

      <!--// geolocation -->
      <!-- vl-geoloc ref="geoloc" @update:position="onUpdatePosition" enableHighAccuracy="true" maximumAge="0" timeout="Infinity" >
        <template slot-scope="geoloc">
          <vl-feature v-if="geoloc.position" id="position-feature" ref="position">
            <vl-geom-point :coordinates="geoloc.position"></vl-geom-point>
            <vl-style-box>
              <vl-style-icon src="statics/marker.png" :scale="0.4" :anchor="[0.5, 1]"></vl-style-icon>
            </vl-style-box>
          </vl-feature>
        </template>
      </vl-geoloc -->
      <!--// geolocation -->

      <!--// base layers -->
      <vl-layer-tile v-for="layer in baseLayers" :key="layer.name" :id="layer.name" :visible="layer.visible">
        <component :is="'vl-source-' + layer.name" v-bind="layer"></component>
      </vl-layer-tile>
      <!--// base layers -->
      <!-- vl-layer-vector-tile ref="layerSource" :declutter="true">
        <vl-source-vector-tile :url="vtUrl"></vl-source-vector-tile -->
        <!-- vl-source-vector-tile :format-factory="createMvtFormat" :url="vtUrl"></vl-source-vector-tile -->
        <!-- vl-source-vector-tile :format-factory="vtFormatFactory" :url="vtUrl"></vl-source-vector-tile -->
        <!-- vl-style-func ref="layerStyle" :factory="getncwellwiseStyle"></vl-style-func>
      </vl-layer-vector-tile -->
      <!--// other layers from config -->
      <!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
      <component v-for="layer in layers" :is="layer.cmp" v-if="layer.visible" :key="layer.id" v-bind="layer">
        <component ref="layerSource" :is="layer.source.cmp" v-bind="layer.source" />
        <!-- component ref="layerSource" :is="layer.source.cmp" v-bind="layer.source" :format-factory="createMvtFormat" / -->
        <component ref="layerStyle" v-if="layer.style" v-for="(style, i) in layer.style" :key="i" :is="style.cmp" v-bind="style" />
      </component>
      <!-- eslint-enable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
    </vl-map>
    <!--// app map -->

    <!--// left side drawer buttons -->
      <q-page-sticky position="top-left" :offset="[58, 18]">
        <q-btn flat dense round icon="fas fa-sign-out-alt" class="bg-teal text-black" aria-label="Dual Screen Map" @click="$router.replace('/dual')">
          <q-tooltip>Go to Side by Side Screen Map</q-tooltip>
        </q-btn>
      </q-page-sticky>
      <q-page-sticky position="top-left" :offset="[18, 18]">
        <q-btn flat dense round icon="menu" class="bg-teal text-black" @click="leftDrawerOpen = !leftDrawerOpen" aria-label="Menu">
          <q-tooltip>Open &amp; Close Side Drawer</q-tooltip>
        </q-btn>
      </q-page-sticky>
    <!--// left side drawer buttons -->

    <!--// ol map controls -->
    <q-page-sticky position="top-left" :offset="[18, 58]">
      <div id="ZoomTarget"></div>
    </q-page-sticky>
    <q-page-sticky position="bottom-left" :offset="[8, 38]">
      <div id="OverviewMapTarget"></div>
    </q-page-sticky>
    <q-page-sticky position="bottom-left" :offset="[15, 8]">
      <div id="ScaleTarget"></div>
    </q-page-sticky>
    <!--// ol map controls -->

    <!--// right side drawer button -->
    <q-page-sticky position="top-right" :offset="[18, 18]">
      <q-btn flat dense round icon="menu" class="bg-teal text-black" @click="rightDrawerOpen = !rightDrawerOpen" aria-label="Menu">
        <q-tooltip>Open &amp; Close Side Drawer</q-tooltip>
      </q-btn>
    </q-page-sticky>
    <q-page-sticky position="top-right" :offset="[18, 58]">
      <q-btn color="teal" class="text-black" @click="$q.fullscreen.toggle()" round :icon="$q.fullscreen.isActive ? 'fullscreen_exit' : 'fullscreen'">
        <q-tooltip>Open &amp; Close Full Screen</q-tooltip>
      </q-btn>
    </q-page-sticky>
    <!--// right side drawer button -->

    <!--// select bar plot tool -->
    <q-page-sticky position="bottom-right" :offset="[18, 18]">
      <q-tooltip>Tools</q-tooltip>
      <q-fab icon="keyboard_arrow_up" direction="up" color="teal text-black">
        <q-tooltip>Test Menu</q-tooltip>
        <q-fab-action color="teal" class="text-black" icon="fas fa-map-marked-alt">
          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
            <q-card class="bg-teal-1">
              <q-banner inline-actions class="bg-teal-1">
                <q-btn color="primary" label="Click me">
                  <q-menu>
                    <q-list dense style="min-width: 100px">
                      <q-item clickable v-close-popup>
                        <q-item-section>Open...</q-item-section>
                      </q-item>
                      <q-item clickable v-close-popup>
                        <q-item-section>New</q-item-section>
                      </q-item>
                      <q-separator></q-separator>
                      <q-item clickable>
                        <q-item-section>Preferences</q-item-section>
                        <q-item-section side>
                          <q-icon name="keyboard_arrow_right"></q-icon>
                        </q-item-section>

                        <q-menu anchor="top end" self="top start">
                          <q-list>
                            <q-item
                              v-for="n in 3"
                              :key="n"
                              dense
                              clickable
                            >
                              <q-item-section>Submenu Label</q-item-section>
                              <q-item-section side>
                                <q-icon name="keyboard_arrow_right"></q-icon>
                              </q-item-section>
                              <q-menu auto-close anchor="top end" self="top start">
                                <q-list>
                                  <q-item
                                    v-for="n in 3"
                                    :key="n"
                                    dense
                                    clickable
                                  >
                                    <q-item-section>3rd level Label</q-item-section>
                                  </q-item>
                                </q-list>
                              </q-menu>
                            </q-item>
                          </q-list>
                        </q-menu>

                      </q-item>
                      <q-separator></q-separator>
                      <q-item clickable v-close-popup>
                        <q-item-section>Quit</q-item-section>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-btn>
                <template align="right" v-slot:action>
                  <q-btn flat round dense icon="close" color="teal" v-close-popup />
                </template>
              </q-banner>
              <q-separator />
            </q-card>
          </q-popup-proxy>
        </q-fab-action>
        <q-tooltip>Change Location</q-tooltip>
        <q-fab-action color="teal" class="text-black" icon="fas fa-map-marked-alt">
          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
            <q-card class="bg-teal-1">
              <q-banner inline-actions class="bg-teal-1">
                <div class="q-pa-md" style="max-width: 400px">
                  <q-form @submit="address2Geoloc" @reset="resetAddress" class="q-gutter-md">
                    <q-input filled v-model="address" label="Address *" hint="Address, City, State and Country" lazy-rules
                      :rules="[ val => val && val.length > 0 || 'Please type something']"
                    ></q-input>
                    <div>
                      <q-btn label="Submit" type="submit" color="teal"></q-btn>
                      <q-btn label="Reset" type="reset" color="teal" flat class="q-ml-sm"></q-btn>
                    </div>
                  </q-form>
                </div>
                <template align="right" v-slot:action>
                  <q-btn flat round dense icon="close" color="teal" v-close-popup />
                </template>
              </q-banner>
              <q-separator />
            </q-card>
          </q-popup-proxy>
        </q-fab-action>
      </q-fab>
    </q-page-sticky>
    <!--// select bar plot tool -->

    <!--// base layer map attribution -->
    <q-page-sticky position="bottom-left" :offset="[200, 38]">
      <div id="AttributionTarget"></div>
    </q-page-sticky>
    <!--// base layer map attribution -->
  </q-layout>
</template>

<script>
// quasar and vuelayers import
import { openURL } from 'quasar'
import { findPointOnSurface, createStyle } from 'vuelayers/lib/ol-ext'
import { camelCase } from 'lodash'

// ol controls import
import ScaleLine from 'ol/control/ScaleLine'
import OverviewMap from 'ol/control/OverviewMap'
import Zoom from 'ol/control/Zoom'
import Attribution from 'ol/control/Attribution'

// Other ol imports
import VectorTile from 'ol/layer/VectorTile'
import Feature from 'ol/Feature'
import MVT from 'ol/format/MVT'
import { Style, Stroke, Fill } from 'ol/style'

// geocoder
const Nominatim = require('nominatim-geocoder')
const geocoder = new Nominatim()

// pubhost and secrets import
import pubhost from '../assets/pubhost.json'
import secrets from '../assets/secrets.json'

let gettoken = function () {
  return secrets[0].MB_KEY
}

export default {
  name: 'NC-Enviroscan',
  components: {
  },
  props: {
    varid: {
      type: String,
      default: ''
    }
  },
  data () {
    return {
      ncCountiesModel: 'Not Selected',
      address: null,
      acceptaddress: false,
      vtSelection: {},
      vtIdProp: 'geoid10',
      apxavgoptions: {
        colors: ['#a534eb', '#eba234', '#747982', '#19800b'],
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 1000
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            type: 'vertical',
            shadeIntensity: 0.05,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 0.9,
            stops: [0, 100]
          }
        },
        chart: {
          toolbar: {
            show: true
          }
        },
        title: {
          text: 'Average Values',
          align: 'left',
          style: {
            color: '#000'
          }
        },
        plotOptions: {
          radialBar: {
            offsetY: 0,
            offsetX: 0,
            startAngle: 0,
            endAngle: 250,
            hollow: {
              margin: 0,
              size: '25%',
              background: 'transparent',
              image: undefined
            },
            dataLabels: {
              name: {
                show: false

              },
              value: {
                show: false
              }
            }
          }
        },
        labels: ['Arsenic', 'Cadmium', 'Lead', 'Manganese'],
        legend: {
          show: true,
          floating: true,
          fontSize: '12px',
          position: 'left',
          offsetX: -20,
          offsetY: 15,
          labels: {
            useSeriesColors: true
          },
          markers: {
            size: 0
          },
          formatter: function (seriesName, opts) {
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppb'
          },
          itemMargin: {
            horizontal: 1
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              show: false
            }
          }
        }]
      },
      apxmedoptions: {
        colors: ['#a534eb', '#eba234', '#747982', '#19800b'],
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 1000
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            type: 'vertical',
            shadeIntensity: 0.05,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 0.9,
            stops: [0, 100]
          }
        },
        chart: {
          toolbar: {
            show: true
          }
        },
        title: {
          text: 'Median Values',
          align: 'left',
          style: {
            color: '#000'
          }
        },
        plotOptions: {
          radialBar: {
            offsetY: 0,
            offsetX: 0,
            startAngle: 0,
            endAngle: 250,
            hollow: {
              margin: 0,
              size: '25%',
              background: 'transparent',
              image: undefined
            },
            dataLabels: {
              name: {
                show: false

              },
              value: {
                show: false
              }
            }
          }
        },
        labels: ['Arsenic', 'Cadmium', 'Lead', 'Manganese'],
        legend: {
          show: true,
          floating: true,
          fontSize: '12px',
          position: 'left',
          offsetX: -20,
          offsetY: 15,
          labels: {
            useSeriesColors: true
          },
          markers: {
            size: 0
          },
          formatter: function (seriesName, opts) {
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppb'
          },
          itemMargin: {
            horizontal: 1
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              show: false
            }
          }
        }]
      },
      apxminoptions: {
        colors: ['#a534eb', '#eba234', '#747982', '#19800b'],
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 1000
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            type: 'vertical',
            shadeIntensity: 0.05,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 0.9,
            stops: [0, 100]
          }
        },
        chart: {
          toolbar: {
            show: true
          }
        },
        title: {
          text: 'Minimum Values',
          align: 'left',
          style: {
            color: '#000'
          }
        },
        plotOptions: {
          radialBar: {
            offsetY: 0,
            offsetX: 0,
            startAngle: 0,
            endAngle: 250,
            hollow: {
              margin: 0,
              size: '25%',
              background: 'transparent',
              image: undefined
            },
            dataLabels: {
              name: {
                show: false

              },
              value: {
                show: false
              }
            }
          }
        },
        labels: ['Arsenic', 'Cadmium', 'Lead', 'Manganese'],
        legend: {
          show: true,
          floating: true,
          fontSize: '12px',
          position: 'left',
          offsetX: -20,
          offsetY: 15,
          labels: {
            useSeriesColors: true
          },
          markers: {
            size: 0
          },
          formatter: function (seriesName, opts) {
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppb'
          },
          itemMargin: {
            horizontal: 1
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              show: false
            }
          }
        }]
      },
      apxmaxoptions: {
        colors: ['#a534eb', '#eba234', '#747982', '#19800b'],
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 1000
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            type: 'vertical',
            shadeIntensity: 0.05,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 0.9,
            stops: [0, 100]
          }
        },
        chart: {
          toolbar: {
            show: true
          }
        },
        title: {
          text: 'Maximum Values',
          align: 'left',
          style: {
            color: '#000'
          }
        },
        plotOptions: {
          radialBar: {
            offsetY: -10,
            offsetX: 0,
            startAngle: 0,
            endAngle: 250,
            hollow: {
              margin: 5,
              size: '30%',
              background: 'transparent',
              image: undefined
            },
            dataLabels: {
              name: {
                show: false

              },
              value: {
                show: false
              }
            }
          }
        },
        labels: ['Arsenic', 'Cadmium', 'Lead', 'Manganese'],
        legend: {
          show: true,
          floating: true,
          fontSize: '16px',
          position: 'left',
          offsetX: -20,
          offsetY: 20,
          labels: {
            useSeriesColors: true
          },
          markers: {
            size: 0
          },
          formatter: function (seriesName, opts) {
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppb'
          },
          itemMargin: {
            horizontal: 1
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              show: false
            }
          }
        }]
      },
      apxstdoptions: {
        colors: ['#a534eb', '#eba234', '#747982', '#19800b'],
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 1000
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            type: 'vertical',
            shadeIntensity: 0.05,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 0.9,
            stops: [0, 100]
          }
        },
        chart: {
          toolbar: {
            show: true
          }
        },
        title: {
          text: 'Standard Deviation Values',
          align: 'left',
          style: {
            color: '#000'
          }
        },
        plotOptions: {
          radialBar: {
            offsetY: 0,
            offsetX: 0,
            startAngle: 0,
            endAngle: 250,
            hollow: {
              margin: 0,
              size: '25%',
              background: 'transparent',
              image: undefined
            },
            dataLabels: {
              name: {
                show: false

              },
              value: {
                show: false
              }
            }
          }
        },
        labels: ['Arsenic', 'Cadmium', 'Lead', 'Manganese'],
        legend: {
          show: true,
          floating: true,
          fontSize: '12px',
          position: 'left',
          offsetX: -20,
          offsetY: 15,
          labels: {
            useSeriesColors: true
          },
          markers: {
            size: 0
          },
          formatter: function (seriesName, opts) {
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppb'
          },
          itemMargin: {
            horizontal: 1
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              show: false
            }
          }
        }]
      },
      // map parameters
      // center: [-73.845, 40.72],
      center: [NaN, NaN],
      zoom: 8,
      rotation: 0,
      mapVisible: true,
      leftDrawerOpen: false,
      rightDrawerOpen: false,
      longitude: null,
      latitude: null,
      pid: undefined,
      // ncwellwise attributes
      /* ncwellwise: {
        'type': 'Feature',
        'properties': {
          'geoid10': undefined,
          'arsenic_med': undefined,
          'arsenic_mean': undefined,
          'arsenic_maximum': undefined,
          'cadmium_med': undefined,
          'cadmium_mean': undefined,
          'cadmium_maximum': undefined,
          'lead_med': undefined,
          'lead_mean': undefined,
          'lead_maximum': undefined,
          'manganese_med': undefined,
          'manganese_mean': undefined,
          'manganese_maximum': undefined
        },
        'geometry': {
          'type': 'MultiPolygonGeom',
          'coordinates': [null, null]
        }
      }, */
      selectedFeature: [],
      selectedFeatureAvgBarBox: [],
      selectedFeatureMedBarBox: [],
      selectedFeatureMinBarBox: [],
      selectedFeatureMaxBarBox: [],
      selectedFeatureStdBarBox: [],
      // state attributes
      eventCoordinate: [NaN, NaN],
      deviceCoordinate: [NaN, NaN],
      coordinateAccuracy: undefined,
      boxCoordinate: undefined,
      // baselayers config
      baselayer: 'osm',
      baseLayers: [
        {
          name: 'osm',
          title: 'OpenStreetMap',
          visible: true
        },
        {
          name: 'mapbox',
          title: 'Mapbox Satellite',
          // mapId: 'mapbox.mapbox-streets-v7',
          mapId: 'mapbox.satellite',
          accessToken: gettoken(),
          visible: false
        }
      ],
      // layers config
      // ncwellwise_arsenic_med: '',
      // ncwellwise_cadmium_med: '',
      currentlayer: 'ncwellwise_arsenic_med',
      ltdblayer: 'pnhblk12',
      // vtUrl: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ncwellwise_subset_20102019_geom.mvt?tile={z}/{x}/{y}',
      layers: [
        {
          id: this.getNCWellwiseLayerID(),
          title: 'NC Wellwise Maximum',
          // cmp: 'vl-layer-vector',
          cmp: 'vl-layer-vector-tile',
          visible: true,
          source: {
            // cmp: 'vl-source-vector',
            cmp: 'vl-source-vector-tile',
            // url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_subset_20102019_geom/?format=json'
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ncwellwise_subset_20102019_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseStyle
            }
          ]
        },
        {
          id: this.getLTDBCensusLayerID(),
          title: 'LTDB Census',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ltdb_std_2012_sample_subset_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getltdbStyle
            }
          ]
        },
        {
          id: this.getEJScreenLayerID(),
          title: 'EJScreen',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ejscreen_subset_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getejscreenStyle
            }
          ]
        },
        {
          id: this.getCovid19LayerID(),
          title: 'Covid19',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/nc_covid_zipcode_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getcovid19Style
            }
          ]
        },
        {
          id: 'ncCounties',
          title: 'NC Counties',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ncdot_county_boundaries.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getNCCountiesStyle
            }
          ]
        }
      ]
    }
  },
  created: function () {
    // get current location, and use it for map center
    this.$getLocation()
      .then(coordinates => {
        this.center = [coordinates.lng, coordinates.lat]
      })
  },
  methods: {
    openURL,
    camelCase,
    pointOnSurface: findPointOnSurface,
    VectorTile,
    Feature,
    createMvtFormat () {
      return new MVT({
        featureClass: Feature
      })
    },
    vtFormatFactory () {
      return new MVT()
    },
    address2Geoloc () {
      // 1 East Edenton St, Raleigh, NC, USA
      geocoder.search({ q: this.address })
        .then((response) => {
          this.center = [Number(response[0].lon), Number(response[0].lat)]
        })
        .catch((error) => {
          console.log(error)
        })
    },
    resetAddress () {
      this.address = null
      this.acceptaddress = false
    },
    onRadarChartAction (params) {
      // console.log(params)
      const { origin, act, payload } = params
      let dothing
      if (this.dimensions[payload] === 'As') {
        dothing = 'Parts Per Million'
      } else if (this.dimensions[payload] === 'Cd') {
        dothing = 'Parts Per Million'
      } else if (this.dimensions[payload] === 'Pb') {
        dothing = 'Parts Per Million'
      } else if (this.dimensions[payload] === 'Mn') {
        dothing = 'Parts Per Thousand'
      }

      switch (act) {
        case origin.ACT_CLICK:
          alert(`Region ${payload} clicked`)
          break
        case origin.ACT_CLICK_DIMENSION_LABEL:
          alert(this.dimensions[payload] + ' ' + dothing)
          break
        default:
          break
      }
    },
    getncwellwiseStyle: function () {
      // console.log(this.currentlayer)
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        // console.log(selected)
        let data = feature.getProperties()
        let color
        if (this.currentlayer === 'ncwellwise_arsenic_med') {
          if (data.arsenic_med === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.arsenic_med < 5) {
            color = 'rgba(235, 52, 220, 0.65)'
          } else if (data.arsenic_med >= 5 && data.arsenic_med < 9) {
            color = 'rgba(186, 52, 235, 0.65)'
          } else if (data.arsenic_med >= 9 && data.arsenic_med < 12) {
            color = 'rgba(165, 52, 235, 0.65)'
          } else if (data.arsenic_med >= 12 && data.arsenic_med < 16) {
            color = 'rgba(143, 52, 235, 0.65)'
          } else if (data.arsenic_med >= 16) {
            color = 'rgba(119, 52, 235, 0.65)'
          }
        } else if (this.currentlayer === 'ncwellwise_arsenic_mean') {
          if (data.arsenic_mean === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.arsenic_mean < 5) {
            color = 'rgba(235, 52, 220, 0.65)'
          } else if (data.arsenic_mean >= 5 && data.arsenic_mean < 9) {
            color = 'rgba(186, 52, 235, 0.65)'
          } else if (data.arsenic_mean >= 9 && data.arsenic_mean < 12) {
            color = 'rgba(165, 52, 235, 0.65)'
          } else if (data.arsenic_mean >= 12 && data.arsenic_mean < 16) {
            color = 'rgba(143, 52, 235, 0.65)'
          } else if (data.arsenic_mean >= 16) {
            color = 'rgba(119, 52, 235, 0.65)'
          }
        } else if (this.currentlayer === 'ncwellwise_cadmium_med') {
          if (data.cadmium_med === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.cadmium_med < 5.0) {
            color = 'rgba(235, 89, 52, 0.65)'
          } else if (data.cadmium_med >= 5.0 && data.cadmium_med < 22.0) {
            color = 'rgba(235, 131, 52, 0.65)'
          } else if (data.cadmium_med >= 22.0 && data.cadmium_med < 33.0) {
            color = 'rgba(235, 162, 52, 0.65)'
          } else if (data.cadmium_med >= 33.0 && data.cadmium_med < 44.0) {
            color = 'rgba(235, 192, 52, 0.65)'
          } else if (data.cadmium_med >= 44.0 && data.cadmium_med < 55.0) {
            color = 'rgba(235, 220, 52, 0.65)'
          } else if (data.cadmium_med >= 55.0) {
            color = 'rgba(223, 235, 52, 0.65)'
          }
        } else if (this.currentlayer === 'ncwellwise_lead_med') {
          if (data.lead_maximum === -999.99) {
            color = 'rgba(50, 110, 219, 0.65)'
          } else if (data.lead_maximum < 11.0) {
            color = 'rgba(196, 200, 207, 0.65)'
          } else if (data.lead_maximum >= 11.0 && data.lead_maximum < 30.0) {
            color = 'rgba(156, 162, 173, 0.65)'
          } else if (data.lead_maximum >= 30.0 && data.lead_maximum < 50.0) {
            color = 'rgba(116, 121, 130, 0.65)'
          } else if (data.lead_maximum >= 50.0 && data.lead_maximum < 80.0) {
            color = 'rgba(79, 82, 89, 0.65)'
          } else if (data.lead_maximum >= 80.0 && data.lead_maximum < 100.0) {
            color = 'rgba(55, 58, 64, 0.65)'
          } else if (data.lead_maximum >= 100.0) {
            color = 'rgba(39, 40, 43, 0.65)'
          }
        } else if (this.currentlayer === 'ncwellwise_mng_med') {
          if (data.manganese_maximum === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.manganese_maximum < 2800.0) {
            color = 'rgba(194, 232, 190, 0.65)'
          } else if (data.manganese_maximum >= 2800.0 && data.manganese_maximum < 5800.0) {
            color = 'rgba(81, 222, 67, 0.65)'
          } else if (data.manganese_maximum >= 5800.0 && data.manganese_maximum < 10800.0) {
            color = 'rgba(25, 128, 11, 0.65)'
          } else if (data.manganese_maximum >= 10800.0 && data.manganese_maximum < 20800.0) {
            color = 'rgba(14, 82, 5, 0.65)'
          } else if (data.manganese_maximum >= 20800.0 && data.manganese_maximum < 40800.0) {
            color = 'rgba(30, 138, 114, 0.65)'
          } else if (data.manganese_maximum >= 40800.0) {
            color = 'rgba(5, 97, 76, 0.65)'
          }
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : color
            })
          })
          /* createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel',
            fillColor: color
          }) */
        ]
      }
    },
    getltdbStyle: function () {
      // console.log(this.currentlayer)
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer.substring(0, 4) === 'hinc') {
          if (data[this.currentlayer] === -999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < 10000) {
            color = 'rgba(252, 210, 211, 0.65)'
          } else if (data[this.currentlayer] >= 10000 && data[this.currentlayer] < 30000) {
            color = 'rgba(252, 109, 114, 0.65)'
          } else if (data[this.currentlayer] >= 30000 && data[this.currentlayer] < 50000) {
            color = 'rgba(247, 59, 66, 0.65)'
          } else if (data[this.currentlayer] >= 50000 && data[this.currentlayer] < 70000) {
            color = 'rgba(250, 2, 11, 0.65)'
          } else if (data[this.currentlayer] >= 70000 && data[this.currentlayer] < 1000000) {
            color = 'rgba(181, 2, 6, 0.65)'
          } else if (data[this.currentlayer] >= 1000000) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else {
          if (data[this.currentlayer] === -999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < 15) {
            color = 'rgba(252, 210, 211, 0.65)'
          } else if (data[this.currentlayer] >= 15 && data[this.currentlayer] < 30) {
            color = 'rgba(252, 109, 114, 0.65)'
          } else if (data[this.currentlayer] >= 30 && data[this.currentlayer] < 45) {
            color = 'rgba(247, 59, 66, 0.65)'
          } else if (data[this.currentlayer] >= 45 && data[this.currentlayer] < 60) {
            color = 'rgba(250, 2, 11, 0.65)'
          } else if (data[this.currentlayer] >= 60 && data[this.currentlayer] < 75) {
            color = 'rgba(181, 2, 6, 0.65)'
          } else if (data[this.currentlayer] >= 75) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : color
            })
          })
          /* createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel',
            fillColor: color
          }) */
        ]
      }
    },
    getejscreenStyle: function () {
      // console.log(this.currentlayer)
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer === 'd_ldpnt_2') {
          if (data[this.currentlayer] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < -200.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer] >= -200.0 && data[this.currentlayer] < 0.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer] >= 0.0 && data[this.currentlayer] < 200.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer] >= 200.0 && data[this.currentlayer] < 400.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer] >= 400.0 && data[this.currentlayer] < 600.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer] >= 600.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer === 'd_dslpm_2') {
          if (data[this.currentlayer] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < -300.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer] >= -300.0 && data[this.currentlayer] < 0.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer] >= 0.0 && data[this.currentlayer] < 280.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer] >= 280.0 && data[this.currentlayer] < 580.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer] >= 580.0 && data[this.currentlayer] < 850.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer] >= 850.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer === 'd_cancr_2') {
          if (data[this.currentlayer] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < -45000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer] >= -45000.0 && data[this.currentlayer] < -20000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer] >= -20000.0 && data[this.currentlayer] < 5000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer] >= 5000.0 && data[this.currentlayer] < 30000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer] >= 30000.0 && data[this.currentlayer] < 55000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer] >= 55000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer === 'd_resp_2') {
          if (data[this.currentlayer] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < -600.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer] >= -600.0 && data[this.currentlayer] < -250) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer] >= -250.0 && data[this.currentlayer] < 100.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer] >= 100.0 && data[this.currentlayer] < 450.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer] >= 450.0 && data[this.currentlayer] < 800.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer] >= 800.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer === 'd_ptraf_2') {
          if (data[this.currentlayer] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < 800000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer] >= 800000.0 && data[this.currentlayer] < 1700000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer] >= 1700000.0 && data[this.currentlayer] < 1700000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer] >= 2600000.0 && data[this.currentlayer] < 2600000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer] >= 3500000.0 && data[this.currentlayer] < 4400000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer] >= 4400000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer === 'd_pwdis_2') {
          if (data[this.currentlayer] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < -47000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer] >= -47000.0 && data[this.currentlayer] < -35000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer] >= -35000.0 && data[this.currentlayer] < -22000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer] >= -22000.0 && data[this.currentlayer] < -10000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer] >= -10000.0 && data[this.currentlayer] < 200.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer] >= 200.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer === 'd_pnpl_2') {
          if (data[this.currentlayer] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < -400.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer] >= -400.0 && data[this.currentlayer] < -120.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer] >= -120.0 && data[this.currentlayer] < 150.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer] >= 150.0 && data[this.currentlayer] < 420.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer] >= 420.0 && data[this.currentlayer] < 690.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer] >= 690.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer === 'd_prmp_2') {
          if (data[this.currentlayer] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < -450.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer] >= -450.0 && data[this.currentlayer] < 1000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer] >= 1000.0 && data[this.currentlayer] < 2450.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer] >= 2450.0 && data[this.currentlayer] < 3900.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer] >= 3900.0 && data[this.currentlayer] < 5350.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer] >= 5350.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer === 'd_ptsdf_2') {
          if (data[this.currentlayer] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < -3200.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer] >= -3200.0 && data[this.currentlayer] < -1000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer] >= -1000.0 && data[this.currentlayer] < 1800.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer] >= 1800.0 && data[this.currentlayer] < 4600.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer] >= 4600.0 && data[this.currentlayer] < 7300.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer] >= 7300.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer === 'd_ozone_2') {
          if (data[this.currentlayer] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < -58000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer] >= -58000.0 && data[this.currentlayer] < -28000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer] >= -28000.0 && data[this.currentlayer] < 600.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer] >= 600.0 && data[this.currentlayer] < 38000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer] >= 38000.0 && data[this.currentlayer] < 70000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer] >= 70000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer === 'd_pm25_2') {
          if (data[this.currentlayer] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < -11000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer] >= -11000.0 && data[this.currentlayer] < -5500.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer] >= -5500.0 && data[this.currentlayer] < 1000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer] >= 1000.0 && data[this.currentlayer] < 7500.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer] >= 7500.0 && data[this.currentlayer] < 15000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer] >= 15000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : color
            })
          })
          /* createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel',
            fillColor: color
          }) */
        ]
      }
    },
    getcovid19Style: function () {
      // console.log(this.currentlayer)
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer === 'cases') {
          if (data[this.currentlayer] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < 1328) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer] >= 1328 && data[this.currentlayer] < 2656) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer] >= 2656 && data[this.currentlayer] < 3984) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer] >= 3984 && data[this.currentlayer] < 5416) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer] >= 5416 && data[this.currentlayer] < 6644) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer] >= 6644) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer === 'cases_per_10000_res') {
          if (data[this.currentlayer] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < 586.0) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer] >= 586.0 && data[this.currentlayer] < 1172.0) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer] >= 1172.0 && data[this.currentlayer] < 1758.0) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer] >= 1758.0 && data[this.currentlayer] < 2344.0) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer] >= 2344.0 && data[this.currentlayer] < 2930.0) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer] >= 2930.0) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer === 'cases_per_100000_res') {
          if (data[this.currentlayer] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < 5859.0) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer] >= 5859.0 && data[this.currentlayer] < 11718.0) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer] >= 11718.0 && data[this.currentlayer] < 17577.0) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer] >= 17577.0 && data[this.currentlayer] < 23436.0) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer] >= 23436.0 && data[this.currentlayer] < 29295.0) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer] >= 29295.0) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer === 'deaths') {
          if (data[this.currentlayer] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer] < 17) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer] >= 17 && data[this.currentlayer] < 34) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer] >= 34 && data[this.currentlayer] < 51) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer] >= 51 && data[this.currentlayer] < 65) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer] >= 65 && data[this.currentlayer] < 85) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer] >= 85) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : color
            })
          })
          /* createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel',
            fillColor: color
          }) */
        ]
      }
    },
    getNCCountiesStyle: function () {
      return feature => {
        return [
          createStyle({
            strokeColor: '#FFFFFF', // '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel'
          })
        ]
      }
    },
    getNCWellwiseLayerID: function () {
      return 'ncwellwise'
    },
    getLTDBCensusLayerID: function () {
      return 'ltdb_census'
    },
    getEJScreenLayerID: function () {
      return 'ejscreen'
    },
    getCovid19LayerID: function () {
      return 'covid19'
    },
    onMapMounted: function (map) {
      // now ol.Map instance is ready and we can work with it directly
      this.$refs.map.$map.getControls().extend([
        new ScaleLine({
          target: 'ScaleTarget'
        }),
        new OverviewMap({
          collapsed: false,
          collapsible: true,
          target: 'OverviewMapTarget'
        }),
        new Zoom({
          target: 'ZoomTarget'
        }),
        new Attribution({
          collapsed: false,
          collapsible: false,
          target: 'AttributionTarget'
        })
      ])
    },
    closeBarChart: function () {
      this.selectedFeature = this.selectedFeature.filter(f => f.id === 0)
      let drawFeatures = this.$refs.drawSource.getFeatures()
      // console.log(drawFeatures)
      this.$refs.drawSource.removeFeatures(drawFeatures)
    },
    // base layers
    showBaseLayer: function () {
      let layer = this.baseLayers.find(layer => layer.visible)
      if (layer != null) {
        layer.visible = false
      }

      layer = this.baseLayers.find(layer => layer.name === this.baselayer)
      if (layer != null) {
        layer.visible = true
      }
    },
    showMapPanelToggleLayer: function () {
      let cntlayer = this.layers[4]
      if (this.ncCountiesModel === 'Selected') {
        cntlayer.visible = true
      } else if (this.ncCountiesModel === 'Not Selected') {
        cntlayer.visible = false
      }
    },
    showMapPanelRadioLayer: function () {
      let layer = this.layers.find(layer => layer.visible)

      if (layer != null) {
        layer.visible = false
      }

      if (this.currentlayer === 'ncwellwise_arsenic_med') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'ncwellwise_arsenic_mean') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'ncwellwise_arsenic_prcast') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'ncwellwise_cadmium_med') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'ncwellwise_cadmium_mean') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'ncwellwise_cadmium_prcast') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'ncwellwise_lead_med') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'ncwellwise_lead_mean') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'ncwellwise_lead_prcast') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'ncwellwise_mng_med') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'ncwellwise_mng_mean') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'ncwellwise_mng_prcast') {
        layer = this.layers.find(layer => layer.id === 'ncwellwise')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'pnhwht12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'pnhblk12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'phisp12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'pasian12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'pntv12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'hincw12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'hincb12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'hinch12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'hinca12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'pwpov12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'pbpov12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'phpov12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'papov12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'pnapov12') {
        layer = this.layers.find(layer => layer.id === 'ltdb_census')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'd_ldpnt_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'd_dslpm_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'd_cancr_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'd_resp_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'd_ptraf_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'd_pwdis_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'd_pnpl_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'd_prmp_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'd_ptsdf_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'd_ozone_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'd_pm25_2') {
        layer = this.layers.find(layer => layer.id === 'ejscreen')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'cases') {
        layer = this.layers.find(layer => layer.id === 'covid19')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'cases_per_10000_res') {
        layer = this.layers.find(layer => layer.id === 'covid19')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'cases_per_100000_res') {
        layer = this.layers.find(layer => layer.id === 'covid19')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (this.currentlayer === 'deaths') {
        layer = this.layers.find(layer => layer.id === 'covid19')
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      }

      if (layer != null) {
        layer.visible = true
      }
    },
    onMapClick: function (event) {
      let pixel = event.pixel
      let features = this.$refs.map.$map.getFeaturesAtPixel(pixel)
      let layer = this.layers.find(layer => layer.visible)
      if (!features) {
        this.vtSelection = {}
        this.selectedFeatureAvgBarBox = []
        this.selectedFeatureMedBarBox = []
        this.selectedFeatureMinBarBox = []
        this.selectedFeatureMaxBarBox = []
        this.selectedFeatureStdBarBox = []
        this.selectedFeature = []
        this.$refs.layerStyle[0].refresh()
        // this.$refs.layerStyle.refresh()
      } else if (features) {
        if (layer.id === 'ncwellwise') {
          this.vtSelection = {}
          this.selectedFeatureAvgBarBox = []
          this.selectedFeatureMedBarBox = []
          this.selectedFeatureMinBarBox = []
          this.selectedFeatureMaxBarBox = []
          this.selectedFeatureStdBarBox = []
          this.eventCoordinate = event.coordinate
          let feature = features[0]
          let fid = feature.get(this.vtIdProp)
          this.vtSelection[fid] = feature
          let properties = feature.getProperties()
          if (properties['geoid10']) {
            this.pid = properties['geoid10']
            this.selectedFeatureMedBarBox.push(properties['arsenic_med'])
            this.selectedFeatureMedBarBox.push(properties['cadmium_med'])
            this.selectedFeatureMedBarBox.push(properties['lead_med'])
            this.selectedFeatureMedBarBox.push(properties['manganese_med'])
            this.selectedFeatureAvgBarBox.push(properties['arsenic_mean'])
            this.selectedFeatureAvgBarBox.push(properties['cadmium_mean'])
            this.selectedFeatureAvgBarBox.push(properties['lead_mean'])
            this.selectedFeatureAvgBarBox.push(properties['manganese_mean'])
            this.selectedFeatureMinBarBox.push(properties['arsenic_minimum'])
            this.selectedFeatureMinBarBox.push(properties['cadmium_minimum'])
            this.selectedFeatureMinBarBox.push(properties['lead_minimum'])
            this.selectedFeatureMinBarBox.push(properties['manganese_minimum'])
            this.selectedFeatureMaxBarBox.push(properties['arsenic_maximum'])
            this.selectedFeatureMaxBarBox.push(properties['cadmium_med'])
            this.selectedFeatureMaxBarBox.push(properties['lead_maximum'])
            this.selectedFeatureMaxBarBox.push(properties['manganese_maximum'])
            this.selectedFeatureStdBarBox.push(properties['arsenic_std'])
            this.selectedFeatureStdBarBox.push(properties['cadmium_std'])
            this.selectedFeatureStdBarBox.push(properties['lead_std'])
            this.selectedFeatureStdBarBox.push(properties['manganese_std'])
          }
          this.$refs.layerStyle[0].refresh()
          // this.$refs.layerStyle.refresh()
        }
      }
    } /* ,
    onUpdatePosition: function (coordinate) {
      this.deviceCoordinate = coordinate
      this.center = [this.deviceCoordinate[0], this.deviceCoordinate[1]]
    },
    onUpdateAccuracy: function (accuracy) {
      this.coordinateAccuracy = accuracy
    } */
  }
}
</script>

<style lang="scss">
  .ol-control button {
    color: black;
    background-color: rgb(0,128,128);
  }
  .ol-control button:hover {
    text-decoration: none;
    background-color: rgb(0,128,128);
  }
  .ol-control button:focus {
    text-decoration: none;
    background-color: rgb(0,128,128);
  }
  .ol-control button:hover, {
    text-decoration: none;
    background-color: rgba(0,128,128,0.8);
  }
  .ol-control button:focus {
    text-decoration: none;
    background-color: rgba(0,128,128,0.8);
  }
  .ol-scale-line {
    background: rgba(0,128,128,0.8);
  }
  a:hover {
    font-weight:bold;
  }
  .wrapper {
    display: flex;
  }
  .map {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
  }
  .view {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
  }
  .feature-popup {
    position: absolute;
    left: -20px;
    bottom: 12px;
    width: 32em;
    max-width: none;
  }
  .feature-popup:after, .feature-popup:before {
    top: 100%;
    border: solid transparent;
    content: ' ';
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
  }
  .feature-popup:after {
    border-top-color: white;
    border-width: 10px;
    left: 48px;
    margin-left: -10px;
  }
  .feature-popup:before {
    border-top-color: #cccccc;
    border-width: 11px;
    left: 48px;
    margin-left: -11px;
  }
  .feature-popup .card-content {
    max-height: 20em;
    overflow: auto;
  }
  .feature-popup .content {
    word-break: break-all;
  }
  .squfill {
    height: 25px;
    width: 25px;
    background-color: rgba(91, 95, 99, 0.65);
    display: inline-block;
  }
  .pbsqufill {
    height: 25px;
    width: 25px;
    background-color: rgba(50, 110, 219, 0.65);
    display: inline-block;
  }
  .assqu1 {
    height: 25px;
    width: 25px;
    background-color: rgba(235, 52, 220, 0.65);
    display: inline-block;
  }
  .assqu2 {
    height: 25px;
    width: 25px;
    background-color: rgba(186, 52, 235, 0.65);
    display: inline-block;
  }
  .assqu3 {
    height: 25px;
    width: 25px;
    background-color: rgba(165, 52, 235, 0.65);
    display: inline-block;
  }
  .assqu4 {
    height: 25px;
    width: 25px;
    background-color: rgba(143, 52, 235, 0.65);
    display: inline-block;
  }
  .assqu5 {
    height: 25px;
    width: 25px;
    background-color: rgba(119, 52, 235, 0.65);
    display: inline-block;
  }
  .cdsqu1 {
    height: 25px;
    width: 25px;
    background-color: rgba(235, 89, 52, 0.65);
    display: inline-block;
  }
  .cdsqu2 {
    height: 25px;
    width: 25px;
    background-color: rgba(235, 131, 52, 0.65);
    display: inline-block;
  }
  .cdsqu3 {
    height: 25px;
    width: 25px;
    background-color: rgba(235, 162, 52, 0.65);
    display: inline-block;
  }
  .cdsqu4 {
    height: 25px;
    width: 25px;
    background-color: rgba(235, 192, 52, 0.65);
    display: inline-block;
  }
  .cdsqu5 {
    height: 25px;
    width: 25px;
    background-color: rgba(235, 220, 52, 0.65);
    display: inline-block;
  }
  .cdsqu6 {
    height: 25px;
    width: 25px;
    background-color: rgba(223, 235, 52, 0.65);
    display: inline-block;
  }
  .pbsqu1 {
    height: 25px;
    width: 25px;
    background-color: rgba(196, 200, 207, 0.65);
    display: inline-block;
  }
  .pbsqu2 {
    height: 25px;
    width: 25px;
    background-color: rgba(156, 162, 173, 0.65);
    display: inline-block;
  }
  .pbsqu3 {
    height: 25px;
    width: 25px;
    background-color: rgba(116, 121, 130, 0.65);
    display: inline-block;
  }
  .pbsqu4 {
    height: 25px;
    width: 25px;
    background-color: rgba(79, 82, 89, 0.65);
    display: inline-block;
  }
  .pbsqu5 {
    height: 25px;
    width: 25px;
    background-color: rgba(55, 58, 64, 0.65);
    display: inline-block;
  }
  .pbsqu6 {
    height: 25px;
    width: 25px;
    background-color: rgba(39, 40, 43, 0.65);
    display: inline-block;
  }
  .mnsqu1 {
    height: 25px;
    width: 25px;
    background-color: rgba(194, 232, 190, 0.65);
    display: inline-block;
  }
  .mnsqu2 {
    height: 25px;
    width: 25px;
    background-color: rgba(81, 222, 67, 0.65);
    display: inline-block;
  }
  .mnsqu3 {
    height: 25px;
    width: 25px;
    background-color: rgba(25, 128, 11, 0.65);
    display: inline-block;
  }
  .mnsqu4 {
    height: 25px;
    width: 25px;
    background-color: rgba(14, 82, 5, 0.65);
    display: inline-block;
  }
  .mnsqu5 {
    height: 25px;
    width: 25px;
    background-color: rgba(30, 138, 114, 0.65);
    display: inline-block;
  }
  .mnsqu6 {
    height: 25px;
    width: 25px;
    background-color: rgba(5, 97, 76, 0.65);
    display: inline-block;
  }
  .q-input {
    height: 4.0em;
  }
  .q-select {
    height: 4.0em;
  }
</style>
