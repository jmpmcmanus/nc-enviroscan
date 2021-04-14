<template>
  <q-layout view="lhr lpr lfr">
    <!--// Left Drawer -->
    <q-drawer v-model="leftDrawerOpen" show-if-above bordered :content-style="{ backgroundColor: 'rgba(199, 235, 235, 0.5)' }">
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeatureAvgBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxavgoptions" :series="selectedFeatureAvgBarBox"></apexchart>
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
                <apexchart width="280" type="radialBar" :options="apxminoptions" :series="selectedFeatureMinBarBox"></apexchart>
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
                <apexchart width="280" type="radialBar" :options="apxmaxoptions" :series="selectedFeatureMaxBarBox"></apexchart>
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
                <apexchart width="280" type="radialBar" :options="apxstdoptions" :series="selectedFeatureStdBarBox"></apexchart>
              </td>
            </tr>
          </div>
        </table>
      </q-card>
    </q-drawer>

    <!--// right side drawer -->
    <q-drawer side="right" v-model="rightDrawerOpen" show-if-above bordered content-class="teal bg-teal-1">
      <q-list bordered class="rounded-borders">
        <!-- // baselayers -->
        <q-expansion-item expand-separator icon="list" label="Base Layers">
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

        <!-- // map 1 layers -->
        <q-expansion-item default-opened expand-separator icon="list" label="Left Side Map Layers">
          <div class="q-pa-md q-gutter-y-sm column">
            <!-- // NC wellwise layers -->
            <q-expansion-item default-opened expand-separator icon="list" label="NC Well Data Layers">
              <div class="q-pa-md q-gutter-y-sm column">
                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="ncwellwise_arsenic_max" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Arsenic Maximum</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="ncwellwise_cadmium_max" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Cadmium Maximum</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="ncwellwise_lead_max" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Lead Maximum</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="ncwellwise_mng_max" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Manganese Maximum</q-item-label>
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
                    <q-radio v-on:input="showMap1PanelLayer" val="pnhwht12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Percent Non-Hispanic White</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="pnhblk12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Percent Non-Hispanic Black</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="phisp12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Percent Hispanic</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="pasian12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Percent Asian</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="pntv12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Percent Native American</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="hincw12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Median HH income, white</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="hincb12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Median HH income, black</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="hinch12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Median HH income, hispanic</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="hinca12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Median HH income, asian</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="pwpov12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>% in poverty, white</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="pbpov12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>% in poverty, black</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="phpov12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>% in poverty, hispanic</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="papov12" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>% in poverty, asian</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="pnapov12" v-model="currentlayer1" color="teal" />
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
                    <q-radio v-on:input="showMap1PanelLayer" val="d_ldpnt_2" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for % pre-1960 housing (lead paint indicator)</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="d_dslpm_2" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Diesel particulate matter level in air</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="d_cancr_2" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Air toxics cancer risk</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="d_resp_2" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Air toxics respiratory hazard index</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="d_ptraf_2" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Traffic proximity and volume</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="d_pwdis_2" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Indicator for major direct dischargers to water</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="d_pnpl_2" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Proximity to National Priorities List (NPL) sites</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="d_prmp_2" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Proximity to Risk Management Plan (RMP) facilities</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="d_ptsdf_2" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Proximity to Treatment Storage and Disposal (TSDF) facilities</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="d_ozone_2" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Ozone level in air</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="d_pm25_2" v-model="currentlayer1" color="teal" />
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
                    <q-radio v-on:input="showMap1PanelLayer" val="cases" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Covid-19 Total Cases</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="cases_per_10000_res" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Covid-19 Cases Per 10,000 Residents</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="cases_per_100000_res" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Covid-19 Cases Per 100,000 Residents-</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap1PanelLayer" val="deaths" v-model="currentlayer1" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Covid-19 Deaths</q-item-label>
                  </q-item-section>
                </q-item>
               </div>
            </q-expansion-item>
            <!-- // Health layers -->

            <!-- // Triangle wellwise layers -->
            <q-expansion-item expand-separator icon="list" label="Triangle Well Data Layers">
              <div class="q-pa-md q-gutter-y-sm column">
                <q-toggle
                  :label="`Arsenic Maximum Layer ${ triwellwiseArsenicMax1Model }`"
                  :key="layers1[4].id"
                  v-on:input="showMap1PanelLayer"
                  :class="{ 'is-active': layers1[4].visible }"
                  color="teal"
                  false-value="Not Selected"
                  true-value="Selected"
                  v-model="triwellwiseArsenicMax1Model"
                />
                <q-toggle
                  :label="`Cadmium Maximum Layer ${ triwellwiseCadmiumMax1Model }`"
                  :key="layers1[5].id"
                  v-on:input="showMap1PanelLayer"
                  :class="{ 'is-active': layers1[5].visible }"
                  color="teal"
                  false-value="Not Selected"
                  true-value="Selected"
                  v-model="triwellwiseCadmiumMax1Model"
                />
              </div>
            </q-expansion-item>
            <!-- // triangle wellwise layers -->
          </div>
        </q-expansion-item>
        <!-- // map 1 layers -->

        <!-- // map 2 layers -->
        <q-expansion-item default-opened expand-separator icon="list" label="Right Side Map Layers">
          <div class="q-pa-md q-gutter-y-sm column">
            <!-- // NC wellwise layers -->
            <q-expansion-item default-opened expand-separator icon="list" label="NC Well Data Layers">
              <div class="q-pa-md q-gutter-y-sm column">
                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="ncwellwise_arsenic_max" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Arsenic Maximum</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="ncwellwise_cadmium_max" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Cadmium Maximum</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="ncwellwise_lead_max" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Lead Maximum</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="ncwellwise_mng_max" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Manganese Maximum</q-item-label>
                  </q-item-section>
                </q-item>
                <!-- q-toggle
                  :label="`Arsenic Maximum Layer ${ ncwellwiseArsenicMax2Model }`"
                  :key="layers2[0].id"
                  v-on:input="showMap2PanelLayer(layers)"
                  :class="{ 'is-active': layers2[0].visible }"
                  color="teal"
                  false-value="Not Selected"
                  true-value="Selected"
                  v-model="ncwellwiseArsenicMax2Model"
                />
                <q-toggle
                  :label="`Cadmium Maximum Layer ${ ncwellwiseCadmiumMax2Model }`"
                  :key="layers2[1].id"
                  v-on:input="showMap2PanelLayer(layers)"
                  :class="{ 'is-active': layers2[1].visible }"
                  color="teal"
                  false-value="Not Selected"
                  true-value="Selected"
                  v-model="ncwellwiseCadmiumMax2Model"
                />
                <q-toggle
                  :label="`Lead Maximum Layer ${ ncwellwiseLeadMax2Model }`"
                  :key="layers2[2].id"
                  v-on:input="showMap2PanelLayer(layers)"
                  :class="{ 'is-active': layers2[2].visible }"
                  color="teal"
                  false-value="Not Selected"
                  true-value="Selected"
                  v-model="ncwellwiseLeadMax2Model"
                />
                <q-toggle
                  :label="`Manganese Maximum Layer ${ ncwellwiseMngMax2Model }`"
                  :key="layers2[3].id"
                  v-on:input="showMap2PanelLayer(layers)"
                  :class="{ 'is-active': layers2[3].visible }"
                  color="teal"
                  false-value="Not Selected"
                  true-value="Selected"
                  v-model="ncwellwiseMngMax2Model"
                / -->
              </div>
            </q-expansion-item>
            <!-- // NC wellwise layers -->

            <!-- // LTDB Census layers -->
            <q-expansion-item expand-separator icon="list" label="Socioeconomic Layers, by Census Tracts">
              <div class="q-pa-md q-gutter-y-sm column">
                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="pnhwht12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Percent Non-Hispanic White</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="pnhblk12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Percent Non-Hispanic Black</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="phisp12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Percent Hispanic</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="pasian12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Percent Asian</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="pntv12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Percent Native American</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="hincw12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Median HH income, white</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="hincb12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Median HH income, black</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="hinch12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Median HH income, hispanic</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="hinca12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Median HH income, asian</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="pwpov12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>% in poverty, white</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="pbpov12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>% in poverty, black</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="phpov12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>% in poverty, hispanic</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="papov12" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>% in poverty, asian</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="pnapov12" v-model="currentlayer2" color="teal" />
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
                    <q-radio v-on:input="showMap2PanelLayer" val="d_ldpnt_2" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for % pre-1960 housing (lead paint indicator)</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="d_dslpm_2" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Diesel particulate matter level in air</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="d_cancr_2" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Air toxics cancer risk</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="d_resp_2" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Air toxics respiratory hazard index</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="d_ptraf_2" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Traffic proximity and volume</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="d_pwdis_2" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Indicator for major direct dischargers to water</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="d_pnpl_2" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Proximity to National Priorities List (NPL) sites</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="d_prmp_2" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Proximity to Risk Management Plan (RMP) facilities</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="d_ptsdf_2" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Proximity to Treatment Storage and Disposal (TSDF) facilities</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="d_ozone_2" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>EJ Index for Ozone level in air</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="d_pm25_2" v-model="currentlayer2" color="teal" />
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
                    <q-radio v-on:input="showMap2PanelLayer" val="cases" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Covid-19 Total Cases</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="cases_per_10000_res" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Covid-19 Cases Per 10,000 Residents</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="cases_per_100000_res" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Covid-19 Cases Per 100,000 Residents-</q-item-label>
                  </q-item-section>
                </q-item>

                <q-item tag="label" v-ripple>
                  <q-item-section avatar>
                    <q-radio v-on:input="showMap2PanelLayer" val="deaths" v-model="currentlayer2" color="teal" />
                  </q-item-section>
                  <q-item-section>
                    <q-item-label>Covid-19 Deaths</q-item-label>
                  </q-item-section>
                </q-item>
               </div>
            </q-expansion-item>
            <!-- // Health layers -->

            <!-- // Triangle wellwise layers -->
            <q-expansion-item expand-separator icon="list" label="Triangle Well Data Layers">
              <div class="q-pa-md q-gutter-y-sm column">
                <q-toggle
                  :label="`Lead Maximum Layer`"
                  :key="layers2[4].id"
                  v-on:input="showMap2PanelLayer"
                  :class="{ 'is-active': layers2[4].visible }"
                  color="teal"
                  false-value="Not Selected"
                  true-value="Selected"
                  v-model="triwellwiseLeadMax2Model"
                />
                <!-- q-toggle
                  :label="`Lead Maximum Layer ${ triwellwiseLeadMax2Model }`"
                  :key="layers2[4].id"
                  v-on:input="showMap2PanelLayer"
                  :class="{ 'is-active': layers2[4].visible }"
                  color="teal"
                  false-value="Not Selected"
                  true-value="Selected"
                  v-model="triwellwiseLeadMax2Model"
                / -->
                <q-toggle
                  :label="`Manganese Maximum Layer ${ triwellwiseManganeseMax2Model }`"
                  :key="layers2[5].id"
                  v-on:input="showMap2PanelLayer"
                  :class="{ 'is-active': layers2[5].visible }"
                  color="teal"
                  false-value="Not Selected"
                  true-value="Selected"
                  v-model="triwellwiseManganeseMax2Model"
                />
              </div>
            </q-expansion-item>
            <!-- // triangle wellwise layers -->
          </div>
        </q-expansion-item>
        <!-- // map 2 layers -->

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
                            <td>&gt; 4</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu2"></span></td>
                            <td>&ge; 4 &amp; &lt; 24</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu3"></span></td>
                            <td>&ge; 24 &amp; &lt; 32</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu4"></span></td>
                            <td>&ge; 32 &amp; &lt; 52</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu5"></span></td>
                            <td>&ge; 52 &amp; &lt; 62</td>
                          </tr>
                          <tr>
                            <td style="padding:5px"><span class="assqu6"></span></td>
                            <td>&ge; 62</td>
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
    <!--// left side drawer -->

    <div class="wrapper">
      <!--// app map1 -->
      <vl-map v-if="mapVisible" class="dualmap" ref="map1" :load-tiles-while-animating="true" :load-tiles-while-interacting="true"
        @click="onMapClick" data-projection="EPSG:4326" @mounted="onMapMounted" :controls="false" style="height:1200px">
        <!--//map1 view aka ol.View -->
        <vl-view ref="view" :center.sync="center" :zoom.sync="zoom" :rotation.sync="rotation"></vl-view>

        <!--// click interactions -->
        <!-- vl-interaction-select ref="selectInteraction" :features.sync="selectedFeature" -->
        <vl-interaction-select ref="selectInteraction" :layers="layer => !(layer instanceof VectorTile)" :features.sync="selectedFeature">
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
                      Feature ID {{ feature.id }} Map 1
                    </div>
                    <template v-slot:action>
                      <q-btn flat round dense icon="close" @click="selectedFeature = selectedFeature.filter(f => f.id !== feature.id)" />
                    </template>
                  </q-banner>
                  <table class="table is-fullwidth">
                    <div v-if="Object.keys(selectedFeatureMaxBarBox).length > 0">
                    <tr>
                      <td>
                        <!-- apexchart width="400" type="radialBar" :options="apxmaxoptions" :series="selectedFeatureMaxBarBox"></apexchart -->
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

          <!--// base layers -->
          <vl-layer-tile v-for="layer in baseLayers" :key="layer.name" :id="layer.name" :visible="layer.visible">
            <component ref="baselayer" :is="'vl-source-' + layer.name" v-bind="layer"></component>
          </vl-layer-tile>
          <!--// base layers -->

          <!--// other layers1 from config -->
          <!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
          <vl-layer-vector-tile v-for="layer in layers1" :is="layer.cmp" v-if="layer.visible" :key="layer.id" v-bind="layer">
            <!--// add vl-source-* -->
            <component :is="layer.source.cmp" v-bind="layer.source" ref="layer1Source" />
            <!--// add style components if provided -->
            <!--// create vl-style-box or vl-style-func -->
            <component v-if="layer.style" v-for="(style, i) in layer.style" :key="i" :is="style.cmp" v-bind="style" ref="layer1Style" />
          </vl-layer-vector-tile>
          <!-- eslint-enable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
          <!--// other layers1 -->
        </vl-map>
        <!--// app map1 -->

        <!--// app map2 -->
        <vl-map v-if="mapVisible" class="dualmap" ref="map2" :load-tiles-while-animating="true" :load-tiles-while-interacting="true"
        @click="onMapClick" data-projection="EPSG:4326" @mounted="onMapMounted" :controls="false" style="height:1200px">
         <!--// map2 view aka ol.View -->
        <vl-view ref="view" :center.sync="center" :zoom.sync="zoom" :rotation.sync="rotation"></vl-view>

        <!--// click interactions -->
        <!-- vl-interaction-select ref="selectInteraction" :features.sync="selectedFeature" -->
        <vl-interaction-select ref="selectInteraction" :layers="layer => !(layer instanceof VectorTile)" :features.sync="selectedFeature">
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
                      Feature ID {{ feature.id }} Map 2
                    </div>
                    <template v-slot:action>
                      <q-btn flat round dense icon="close" @click="selectedFeature = selectedFeature.filter(f => f.id !== feature.id)" />
                    </template>
                  </q-banner>
                  <table class="table is-fullwidth">
                    <div v-if="Object.keys(selectedFeatureMaxBarBox).length > 0">
                    <tr>
                      <td>
                        <apexchart width="400" type="radialBar" :options="apxmaxoptions" :series="selectedFeatureMaxBarBox"></apexchart>
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

        <!--// base layers2 -->
        <vl-layer-tile v-for="layer in baseLayers" :key="layer.name" :id="layer.name" :visible="layer.visible">
          <component :is="'vl-source-' + layer.name" v-bind="layer"></component>
        </vl-layer-tile>
        <!--// base layers -->

        <!--// other layers2 from config -->
        <!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
        <component v-for="layer in layers2" :is="layer.cmp" v-if="layer.visible" :key="layer.id" v-bind="layer">
          <!--// add vl-source-* -->
          <component ref="layer2Source" :is="layer.source.cmp" v-bind="layer.source">
          </component>

          <!--// add style components if provided -->
          <!--// create vl-style-box or vl-style-func -->
          <component ref="layer2Style" v-if="layer.style" v-for="(style, i) in layer.style" :key="i" :is="style.cmp" v-bind="style">
          </component>
        </component>
        <!-- eslint-enable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
        <!--// other layers2 -->
      </vl-map>
      <!--// app map2 -->
    </div>

    <!--// left side drawer buttons -->
      <q-page-sticky position="top-left" :offset="[58, 18]">
        <q-btn flat dense round icon="fas fa-sign-out-alt" class="bg-teal text-black" aria-label="Single Screen Map" @click="$router.replace('/')">
          <q-tooltip>Go to Single Screen Map</q-tooltip>
        </q-btn>
      </q-page-sticky>
      <q-page-sticky position="top-left" :offset="[18, 18]">
        <q-btn flat dense round icon="menu" class="bg-teal text-black" @click="leftDrawerOpen = !leftDrawerOpen" aria-label="Menu">
          <q-tooltip>Open &amp; Close Side Drawer</q-tooltip>
        </q-btn>
      </q-page-sticky>
    <!--// left side drawer buttons -->

    <!--// ol map1 controls -->
    <q-page-sticky position="top-left" :offset="[18, 58]">
      <div id="Zoom1Target"></div>
    </q-page-sticky>
    <q-page-sticky position="bottom-left" :offset="[8, 38]">
      <div id="OverviewMap1Target"></div>
    </q-page-sticky>
    <q-page-sticky position="bottom-left" :offset="[15, 8]">
      <div id="Scale1Target"></div>
    </q-page-sticky>
    <!--// ol map1 controls -->

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

    <!--// select radial bar plot tool -->
    <q-page-sticky position="bottom-right" :offset="[18, 18]">
      <q-tooltip>Tools</q-tooltip>
      <q-fab icon="keyboard_arrow_up" direction="up" color="teal text-black">
        <q-tooltip>Select Box</q-tooltip>
        <q-fab-action color="teal" class="text-black" icon="fas fa-vector-square">
          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
            <q-card class="bg-teal-1">
              <q-banner inline-actions class="bg-teal-1">
                <div class="text-subtitle2">
                  Create Bar Plot of Selected Features
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

// other ol imports
import VectorTile from 'ol/layer/VectorTile'
import { Style, Stroke, Fill } from 'ol/style'
import { DEVICE_PIXEL_RATIO } from 'ol/has.js'

// pubhost and secrets import
import pubhost from '../assets/pubhost.json'
import secrets from '../assets/secrets.json'

let gettoken = function () {
  return secrets[0].MB_KEY
}

export default {
  name: 'NC-Enviroscan-Dual',
  components: {
  },
  data () {
    return {
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
      zoom: 9,
      rotation: 0,
      mapVisible: true,
      leftDrawerOpen: false,
      rightDrawerOpen: false,
      longitude: null,
      latitude: null,
      pid: undefined,
      // ncwellwise attributes
      ncwellwise: {
        'type': 'Feature',
        'properties': {
          'geoid10': undefined,
          'arsenic_mean': undefined,
          'arsenic_maximum': undefined,
          'cadmium_mean': undefined,
          'cadmium_maximum': undefined,
          'lead_mean': undefined,
          'lead_maximum': undefined,
          'manganese_mean': undefined,
          'manganese_maximum': undefined
        },
        'geometry': {
          'type': 'MultiPolygonGeom',
          'coordinates': [null, null]
        }
      },
      triwellwiseArsenicMax1Model: 'Not Selected',
      triwellwiseCadmiumMax1Model: 'Not Selected',
      triwellwiseLeadMax2Model: 'Not Selected',
      triwellwiseManganeseMax2Model: 'Not Selected',
      ttitle: undefined,
      // stored and selected features
      storeFeatures: [],
      selectedFeature: [],
      selectedFeatureMaxBarBox: [],
      selectedFeatureAvgBarBox: [],
      selectedFeatureMinBarBox: [],
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
      currentlayer1: 'ncwellwise_arsenic_max',
      currentlayer2: 'ncwellwise_arsenic_max',
      currentvar2: 'lead_maximum',
      layers1: [
        {
          id: this.getNCWellwiseLayer1ID(),
          title: 'NC Wellwise Layer 1 Maximum',
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
              factory: this.getncwellwiseStyle1
            }
          ]
        },
        {
          id: this.getLTDBCensusLayer1ID(),
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
              factory: this.getltdbStyle1
            }
          ]
        },
        {
          id: this.getEJScreenLayer1ID(),
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
              factory: this.getejscreenStyle1
            }
          ]
        },
        {
          id: this.getCovid19Layer1ID(),
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
              factory: this.getcovid19Style1
            }
          ]
        },
        {
          id: 'triwellwise_arsenic_max',
          title: 'trianle wellwise Arsenic Maximum',
          cmp: 'vl-layer-vector',
          visible: false,
          source: {
            cmp: 'vl-source-vector',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_triangle_20102019_geom/?format=json'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseArsenicMaxStyle
            }
          ]
        },
        {
          id: 'triwellwise_cadmium_max',
          title: 'Triangle Wellwise Cadmium Maximum',
          cmp: 'vl-layer-vector',
          visible: false,
          source: {
            cmp: 'vl-source-vector',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_triangle_20102019_geom/?format=json'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseCadmiumMaxStyle
            }
          ]
        }
      ],
      layers2: [
        {
          id: this.getNCWellwiseLayer2ID(),
          title: 'NC Wellwise Layer 2 Maximum',
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
              factory: this.getncwellwiseStyle2
            }
          ]
        },
        {
          id: this.getLTDBCensusLayer2ID(),
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
              factory: this.getltdbStyle2
            }
          ]
        },
        {
          id: this.getEJScreenLayer2ID(),
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
              factory: this.getejscreenStyle2
            }
          ]
        },
        {
          id: this.getCovid19Layer2ID(),
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
              factory: this.getcovid19Style2
            }
          ]
        },
        {
          id: 'triwellwise_lead_max',
          title: 'Trianel wellwise Lead Maximum',
          cmp: 'vl-layer-vector',
          visible: false,
          source: {
            cmp: 'vl-source-vector',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_subset_20102019_geom/?format=json'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseLeadMaxStyle
            }
          ]
        },
        {
          id: 'triwellwise_mng_max',
          title: 'Triangle Wellwise Manganese Maximum',
          cmp: 'vl-layer-vector',
          visible: false,
          source: {
            cmp: 'vl-source-vector',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_subset_20102019_geom/?format=json'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseMngMaxStyle
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
    getncwellwiseStyle1: function () {
      /* let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO
      let that = this
      function getPattern (color1) {
        canvas.width = 8 * pixelRatio
        canvas.height = 8 * pixelRatio
        let color2 = 'rgb(0, 0, 0, 0.0)'
        let numberOfStripes = 50
        var i
        var thickness
        if (that.currentlayer1 === 'ncwellwise_arsenic_max') {
          for (i = 0; i < numberOfStripes * 2; i++) {
            thickness = 200 / numberOfStripes
            context.beginPath()
            context.strokeStyle = i % 2 ? color1 : color2
            context.lineWidth = thickness
            context.lineCap = 'round'

            context.moveTo(i * thickness * pixelRatio + thickness / 2 - 300, 0)
            context.lineTo(0 + i * thickness * pixelRatio + thickness / 2, 300)
            context.stroke()
          }
        } else if (that.currentlayer1 === 'ncwellwise_cadmium_max') {
          for (i = 0; i < numberOfStripes; i++) {
            thickness = 200 / numberOfStripes
            context.beginPath()
            context.strokeStyle = i % 2 ? color1 : color2
            context.lineWidth = thickness
            context.lineCap = 'round'

            context.moveTo(i * thickness + thickness / 2, 0)
            context.lineTo(i * thickness + thickness / 2, 300)
            context.stroke()
          }
        } else if (that.currentlayer1 === 'ncwellwise_lead_max') {
          for (i = 0; i < numberOfStripes * 2; i++) {
            thickness = 200 / numberOfStripes
            context.beginPath()
            context.strokeStyle = i % 2 ? color1 : color2
            context.lineWidth = thickness
            context.lineCap = 'round'

            context.moveTo(i * thickness * pixelRatio + thickness / 2 - 300, 300)
            context.lineTo(0 + i * thickness * pixelRatio + thickness / 2, 0)
            context.stroke()
          }
        } else if (that.currentlayer1 === 'ncwellwise_mng_max') {
          for (i = 0; i < numberOfStripes; i++) {
            thickness = 200 / numberOfStripes
            context.beginPath()
            context.strokeStyle = i % 2 ? color1 : color2
            context.lineWidth = thickness
            context.lineCap = 'round'

            context.moveTo(0, i * thickness + thickness / 2)
            context.lineTo(300, i * thickness + thickness / 2)
            context.stroke()
          }
        }
        return context.createPattern(canvas, 'repeat')
      } */
      return feature => {
        let data = feature.getProperties()
        let color
        if (this.currentlayer1 === 'ncwellwise_arsenic_max') {
          if (data.arsenic_maximum === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.arsenic_maximum < 4) {
            color = 'rgba(119, 52, 235, 0.65)'
          } else if (data.arsenic_maximum >= 4 && data.arsenic_maximum < 24) {
            color = 'rgba(143, 52, 235, 0.65)'
          } else if (data.arsenic_maximum >= 24 && data.arsenic_maximum < 32) {
            color = 'rgba(165, 52, 235, 0.65)'
          } else if (data.arsenic_maximum >= 32 && data.arsenic_maximum < 52) {
            color = 'rgba(186, 52, 235, 0.65)'
          } else if (data.arsenic_maximum >= 52 && data.arsenic_maximum < 62) {
            color = 'rgba(211, 52, 235, 0.65)'
          } else if (data.arsenic_maximum >= 62) {
            color = 'rgba(235, 52, 220, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_cadmium_max') {
          if (data.cadmium_maximum === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.cadmium_maximum < 5.0) {
            color = 'rgba(235, 89, 52, 0.65)'
          } else if (data.cadmium_maximum >= 5.0 && data.cadmium_maximum < 22.0) {
            color = 'rgba(235, 131, 52, 0.65)'
          } else if (data.cadmium_maximum >= 22.0 && data.cadmium_maximum < 33.0) {
            color = 'rgba(235, 162, 52, 0.65)'
          } else if (data.cadmium_maximum >= 33.0 && data.cadmium_maximum < 44.0) {
            color = 'rgba(235, 192, 52, 0.65)'
          } else if (data.cadmium_maximum >= 44.0 && data.cadmium_maximum < 55.0) {
            color = 'rgba(235, 220, 52, 0.65)'
          } else if (data.cadmium_maximum >= 55.0) {
            color = 'rgba(223, 235, 52, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_lead_max') {
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
        } else if (this.currentlayer1 === 'ncwellwise_mng_max') {
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
        /* if (this.currentlayer1 === 'ncwellwise_arsenic_max') {
          if (data.arsenic_maximum === -999.99) {
            color = getPattern('rgba(91, 95, 99, 0.65)')
          } else if (data.arsenic_maximum < 4) {
            color = getPattern('rgba(119, 52, 235, 0.65)')
          } else if (data.arsenic_maximum >= 4 && data.arsenic_maximum < 24) {
            color = getPattern('rgba(143, 52, 235, 0.65)')
          } else if (data.arsenic_maximum >= 24 && data.arsenic_maximum < 32) {
            color = getPattern('rgba(165, 52, 235, 0.65)')
          } else if (data.arsenic_maximum >= 32 && data.arsenic_maximum < 52) {
            color = getPattern('rgba(186, 52, 235, 0.65)')
          } else if (data.arsenic_maximum >= 52 && data.arsenic_maximum < 62) {
            color = getPattern('rgba(211, 52, 235, 0.65)')
          } else if (data.arsenic_maximum >= 62) {
            color = getPattern('rgba(235, 52, 220, 0.65)')
          }
        } else if (this.currentlayer1 === 'ncwellwise_cadmium_max') {
          if (data.cadmium_maximum === -999.99) {
            color = getPattern('rgba(91, 95, 99, 0.65)')
          } else if (data.cadmium_maximum < 5.0) {
            color = getPattern('rgba(235, 89, 52, 0.65)')
          } else if (data.cadmium_maximum >= 5.0 && data.cadmium_maximum < 22.0) {
            color = getPattern('rgba(235, 131, 52, 0.65)')
          } else if (data.cadmium_maximum >= 22.0 && data.cadmium_maximum < 33.0) {
            color = getPattern('rgba(235, 162, 52, 0.65)')
          } else if (data.cadmium_maximum >= 33.0 && data.cadmium_maximum < 44.0) {
            color = getPattern('rgba(235, 192, 52, 0.65)')
          } else if (data.cadmium_maximum >= 44.0 && data.cadmium_maximum < 55.0) {
            color = getPattern('rgba(235, 220, 52, 0.65)')
          } else if (data.cadmium_maximum >= 55.0) {
            color = getPattern('rgba(223, 235, 52, 0.65)')
          }
        } else if (this.currentlayer1 === 'ncwellwise_lead_max') {
          if (data.lead_maximum === -999.99) {
            color = getPattern('rgba(50, 110, 219, 0.65)')
          } else if (data.lead_maximum < 11.0) {
            color = getPattern('rgba(196, 200, 207, 0.65)')
          } else if (data.lead_maximum >= 11.0 && data.lead_maximum < 30.0) {
            color = getPattern('rgba(156, 162, 173, 0.65)')
          } else if (data.lead_maximum >= 30.0 && data.lead_maximum < 50.0) {
            color = getPattern('rgba(116, 121, 130, 0.65)')
          } else if (data.lead_maximum >= 50.0 && data.lead_maximum < 80.0) {
            color = getPattern('rgba(79, 82, 89, 0.65)')
          } else if (data.lead_maximum >= 80.0 && data.lead_maximum < 100.0) {
            color = getPattern('rgba(55, 58, 64, 0.65)')
          } else if (data.lead_maximum >= 100.0) {
            color = getPattern('rgba(39, 40, 43, 0.65)')
          }
        } else if (this.currentlayer1 === 'ncwellwise_mng_max') {
          if (data.manganese_maximum === -999.99) {
            color = getPattern('rgba(91, 95, 99, 0.65)')
          } else if (data.manganese_maximum < 2800.0) {
            color = getPattern('rgba(194, 232, 190, 0.65)')
          } else if (data.manganese_maximum >= 2800.0 && data.manganese_maximum < 5800.0) {
            color = getPattern('rgba(81, 222, 67, 0.65)')
          } else if (data.manganese_maximum >= 5800.0 && data.manganese_maximum < 10800.0) {
            color = getPattern('rgba(25, 128, 11, 0.65)')
          } else if (data.manganese_maximum >= 10800.0 && data.manganese_maximum < 20800.0) {
            color = getPattern('rgba(14, 82, 5, 0.65)')
          } else if (data.manganese_maximum >= 20800.0 && data.manganese_maximum < 40800.0) {
            color = getPattern('rgba(30, 138, 114, 0.65)')
          } else if (data.manganese_maximum >= 40800.0) {
            color = getPattern('rgba(5, 97, 76, 0.65)')
          }
        } */
        const ncwellwise = [
          createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel',
            fillColor: color
          })
        ]
        return ncwellwise
      }
    },
    getltdbStyle1: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer1.substring(0, 4) === 'hinc') {
          if (data[this.currentlayer1] === -999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < 10000) {
            color = 'rgba(252, 210, 211, 0.65)'
          } else if (data[this.currentlayer1] >= 10000 && data[this.currentlayer1] < 30000) {
            color = 'rgba(252, 109, 114, 0.65)'
          } else if (data[this.currentlayer1] >= 30000 && data[this.currentlayer1] < 50000) {
            color = 'rgba(247, 59, 66, 0.65)'
          } else if (data[this.currentlayer1] >= 50000 && data[this.currentlayer1] < 70000) {
            color = 'rgba(250, 2, 11, 0.65)'
          } else if (data[this.currentlayer1] >= 70000 && data[this.currentlayer1] < 1000000) {
            color = 'rgba(181, 2, 6, 0.65)'
          } else if (data[this.currentlayer1] >= 1000000) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else {
          if (data[this.currentlayer1] === -999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < 15) {
            color = 'rgba(252, 210, 211, 0.65)'
          } else if (data[this.currentlayer1] >= 15 && data[this.currentlayer1] < 30) {
            color = 'rgba(252, 109, 114, 0.65)'
          } else if (data[this.currentlayer1] >= 30 && data[this.currentlayer1] < 45) {
            color = 'rgba(247, 59, 66, 0.65)'
          } else if (data[this.currentlayer1] >= 45 && data[this.currentlayer1] < 60) {
            color = 'rgba(250, 2, 11, 0.65)'
          } else if (data[this.currentlayer1] >= 60 && data[this.currentlayer1] < 75) {
            color = 'rgba(181, 2, 6, 0.65)'
          } else if (data[this.currentlayer1] >= 75) {
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
    getejscreenStyle1: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer1 === 'd_ldpnt_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -200.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -200.0 && data[this.currentlayer1] < 0.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 0.0 && data[this.currentlayer1] < 200.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 200.0 && data[this.currentlayer1] < 400.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 400.0 && data[this.currentlayer1] < 600.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 600.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_dslpm_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -300.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -300.0 && data[this.currentlayer1] < 0.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 0.0 && data[this.currentlayer1] < 280.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 280.0 && data[this.currentlayer1] < 580.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 580.0 && data[this.currentlayer1] < 850.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 850.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_cancr_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -45000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -45000.0 && data[this.currentlayer1] < -20000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -20000.0 && data[this.currentlayer1] < 5000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 5000.0 && data[this.currentlayer1] < 30000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 30000.0 && data[this.currentlayer1] < 55000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 55000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_resp_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -600.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -600.0 && data[this.currentlayer1] < -250) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -250.0 && data[this.currentlayer1] < 100.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 100.0 && data[this.currentlayer1] < 450.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 450.0 && data[this.currentlayer1] < 800.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 800.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_ptraf_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < 800000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 800000.0 && data[this.currentlayer1] < 1700000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 1700000.0 && data[this.currentlayer1] < 1700000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 2600000.0 && data[this.currentlayer1] < 2600000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 3500000.0 && data[this.currentlayer1] < 4400000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 4400000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_pwdis_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -47000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -47000.0 && data[this.currentlayer1] < -35000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -35000.0 && data[this.currentlayer1] < -22000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -22000.0 && data[this.currentlayer1] < -10000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -10000.0 && data[this.currentlayer1] < 200.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 200.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_pnpl_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -400.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -400.0 && data[this.currentlayer1] < -120.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -120.0 && data[this.currentlayer1] < 150.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 150.0 && data[this.currentlayer1] < 420.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 420.0 && data[this.currentlayer1] < 690.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 690.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_prmp_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -450.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -450.0 && data[this.currentlayer1] < 1000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 1000.0 && data[this.currentlayer1] < 2450.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 2450.0 && data[this.currentlayer1] < 3900.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 3900.0 && data[this.currentlayer1] < 5350.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 5350.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_ptsdf_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -3200.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -3200.0 && data[this.currentlayer1] < -1000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -1000.0 && data[this.currentlayer1] < 1800.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 1800.0 && data[this.currentlayer1] < 4600.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 4600.0 && data[this.currentlayer1] < 7300.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 7300.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_ozone_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -58000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -58000.0 && data[this.currentlayer1] < -28000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -28000.0 && data[this.currentlayer1] < 600.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 600.0 && data[this.currentlayer1] < 38000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 38000.0 && data[this.currentlayer1] < 70000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 70000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_pm25_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -11000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -11000.0 && data[this.currentlayer1] < -5500.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -5500.0 && data[this.currentlayer1] < 1000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 1000.0 && data[this.currentlayer1] < 7500.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 7500.0 && data[this.currentlayer1] < 15000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 15000.0) {
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
    getcovid19Style1: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer1 === 'cases') {
          if (data[this.currentlayer1] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < 1328) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer1] >= 1328 && data[this.currentlayer1] < 2656) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 2656 && data[this.currentlayer1] < 3984) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 3984 && data[this.currentlayer1] < 5416) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 5416 && data[this.currentlayer1] < 6644) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 6644) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer1 === 'cases_per_10000_res') {
          if (data[this.currentlayer1] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < 586.0) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer1] >= 586.0 && data[this.currentlayer1] < 1172.0) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 1172.0 && data[this.currentlayer1] < 1758.0) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 1758.0 && data[this.currentlayer1] < 2344.0) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 2344.0 && data[this.currentlayer1] < 2930.0) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 2930.0) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer1 === 'cases_per_100000_res') {
          if (data[this.currentlayer1] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < 5859.0) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer1] >= 5859.0 && data[this.currentlayer1] < 11718.0) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 11718.0 && data[this.currentlayer1] < 17577.0) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 17577.0 && data[this.currentlayer1] < 23436.0) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 23436.0 && data[this.currentlayer1] < 29295.0) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 29295.0) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer1 === 'deaths') {
          if (data[this.currentlayer1] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < 17) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer1] >= 17 && data[this.currentlayer1] < 34) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 34 && data[this.currentlayer1] < 51) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 51 && data[this.currentlayer1] < 65) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 65 && data[this.currentlayer1] < 85) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 85) {
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
    getncwellwiseArsenicMaxStyle: function () {
      let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO

      function getPattern (color2) {
        canvas.width = 8 * pixelRatio
        canvas.height = 8 * pixelRatio
        let color1 = 'rgb(0, 0, 0, 0.0)'
        let numberOfStripes = 50
        for (var i = 0; i < numberOfStripes; i++) {
          var thickness = 200 / numberOfStripes
          context.beginPath()
          context.strokeStyle = i % 2 ? color1 : color2
          context.lineWidth = thickness
          context.lineCap = 'round'

          context.moveTo(i * thickness + thickness / 2, 0)
          context.lineTo(i * thickness + thickness / 2, 300)
          context.stroke()
        }
        return context.createPattern(canvas, 'repeat')
      }
      return feature => {
        let data = feature.getProperties()
        let color
        if (data.arsenic_maximum === -999.99) {
          color = 'rgba(91, 95, 99, 1.0)'
        } else if (data.arsenic_maximum < 4) {
          color = getPattern('rgba(119, 52, 235, 1.0)')
        } else if (data.arsenic_maximum >= 4 && data.arsenic_maximum < 24) {
          color = getPattern('rgba(143, 52, 235, 1.)')
        } else if (data.arsenic_maximum >= 24 && data.arsenic_maximum < 32) {
          color = getPattern('rgba(165, 52, 235, 1.0)')
        } else if (data.arsenic_maximum >= 32 && data.arsenic_maximum < 52) {
          color = getPattern('rgba(186, 52, 235, 1.0)')
        } else if (data.arsenic_maximum >= 52 && data.arsenic_maximum < 62) {
          color = getPattern('rgba(211, 52, 235, 1.0)')
        } else if (data.arsenic_maximum >= 62) {
          color = getPattern('rgba(235, 52, 220, 1.0)')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: '#000',
              width: (this.zoom / 8.0),
              lineCap: 'round',
              lineJoin: 'bevel'
            }),
            fill: new Fill({
              color: color
            })
          })
        ]
      }
    },
    getncwellwiseCadmiumMaxStyle: function () {
      let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO

      function getPattern (color1) {
        canvas.width = 8 * pixelRatio
        canvas.height = 8 * pixelRatio
        let color2 = 'rgb(0, 0, 0, 0.0)'
        let numberOfStripes = 50
        for (var i = 0; i < numberOfStripes; i++) {
          var thickness = 200 / numberOfStripes
          context.beginPath()
          context.strokeStyle = i % 2 ? color1 : color2
          context.lineWidth = thickness
          context.lineCap = 'round'

          context.moveTo(i * thickness + thickness / 2, 0)
          context.lineTo(i * thickness + thickness / 2, 300)
          context.stroke()
        }
        return context.createPattern(canvas, 'repeat')
      }
      return feature => {
        let data = feature.getProperties()
        let color
        if (data.cadmium_maximum === -999.99) {
          color = 'rgba(91, 95, 99, 1.0)'
        } else if (data.cadmium_maximum < 5.0) {
          color = getPattern('rgba(235, 89, 52, 1.0)')
        } else if (data.cadmium_maximum >= 5.0 && data.cadmium_maximum < 22.0) {
          color = getPattern('rgba(235, 131, 52, 1.0)')
        } else if (data.cadmium_maximum >= 22.0 && data.cadmium_maximum < 33.0) {
          color = getPattern('rgba(235, 162, 52, 1.0)')
        } else if (data.cadmium_maximum >= 33.0 && data.cadmium_maximum < 44.0) {
          color = getPattern('rgba(235, 192, 52, 1.0)')
        } else if (data.cadmium_maximum >= 44.0 && data.cadmium_maximum < 55.0) {
          color = getPattern('rgba(235, 220, 52, 1.0)')
        } else if (data.cadmium_maximum >= 55.0) {
          color = getPattern('rgba(223, 235, 52, 1.0)')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: '#000',
              width: (this.zoom / 8.0),
              lineCap: 'round',
              lineJoin: 'bevel'
            }),
            fill: new Fill({
              color: color
            })
          })
        ]
      }
    },
    getncwellwiseStyle2: function () {
      return feature => {
        let data = feature.getProperties()
        let color
        if (this.currentlayer2 === 'ncwellwise_arsenic_max') {
          if (data.arsenic_maximum === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.arsenic_maximum < 4) {
            color = 'rgba(119, 52, 235, 0.65)'
          } else if (data.arsenic_maximum >= 4 && data.arsenic_maximum < 24) {
            color = 'rgba(143, 52, 235, 0.65)'
          } else if (data.arsenic_maximum >= 24 && data.arsenic_maximum < 32) {
            color = 'rgba(165, 52, 235, 0.65)'
          } else if (data.arsenic_maximum >= 32 && data.arsenic_maximum < 52) {
            color = 'rgba(186, 52, 235, 0.65)'
          } else if (data.arsenic_maximum >= 52 && data.arsenic_maximum < 62) {
            color = 'rgba(211, 52, 235, 0.65)'
          } else if (data.arsenic_maximum >= 62) {
            color = 'rgba(235, 52, 220, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_cadmium_max') {
          if (data.cadmium_maximum === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.cadmium_maximum < 5.0) {
            color = 'rgba(235, 89, 52, 0.65)'
          } else if (data.cadmium_maximum >= 5.0 && data.cadmium_maximum < 22.0) {
            color = 'rgba(235, 131, 52, 0.65)'
          } else if (data.cadmium_maximum >= 22.0 && data.cadmium_maximum < 33.0) {
            color = 'rgba(235, 162, 52, 0.65)'
          } else if (data.cadmium_maximum >= 33.0 && data.cadmium_maximum < 44.0) {
            color = 'rgba(235, 192, 52, 0.65)'
          } else if (data.cadmium_maximum >= 44.0 && data.cadmium_maximum < 55.0) {
            color = 'rgba(235, 220, 52, 0.65)'
          } else if (data.cadmium_maximum >= 55.0) {
            color = 'rgba(223, 235, 52, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_lead_max') {
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
        } else if (this.currentlayer2 === 'ncwellwise_mng_max') {
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
        const ncwellwise = [
          createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel',
            fillColor: color
          })
        ]
        return ncwellwise
      }
    },
    getltdbStyle2: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer2.substring(0, 4) === 'hinc') {
          if (data[this.currentlayer2] === -999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < 10000) {
            color = 'rgba(252, 210, 211, 0.65)'
          } else if (data[this.currentlayer2] >= 10000 && data[this.currentlayer2] < 30000) {
            color = 'rgba(252, 109, 114, 0.65)'
          } else if (data[this.currentlayer2] >= 30000 && data[this.currentlayer2] < 50000) {
            color = 'rgba(247, 59, 66, 0.65)'
          } else if (data[this.currentlayer2] >= 50000 && data[this.currentlayer2] < 70000) {
            color = 'rgba(250, 2, 11, 0.65)'
          } else if (data[this.currentlayer2] >= 70000 && data[this.currentlayer2] < 1000000) {
            color = 'rgba(181, 2, 6, 0.65)'
          } else if (data[this.currentlayer2] >= 1000000) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else {
          if (data[this.currentlayer2] === -999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < 15) {
            color = 'rgba(252, 210, 211, 0.65)'
          } else if (data[this.currentlayer2] >= 15 && data[this.currentlayer2] < 30) {
            color = 'rgba(252, 109, 114, 0.65)'
          } else if (data[this.currentlayer2] >= 30 && data[this.currentlayer2] < 45) {
            color = 'rgba(247, 59, 66, 0.65)'
          } else if (data[this.currentlayer2] >= 45 && data[this.currentlayer2] < 60) {
            color = 'rgba(250, 2, 11, 0.65)'
          } else if (data[this.currentlayer2] >= 60 && data[this.currentlayer2] < 75) {
            color = 'rgba(181, 2, 6, 0.65)'
          } else if (data[this.currentlayer2] >= 75) {
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

        ]
      }
    },
    getejscreenStyle2: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer2 === 'd_ldpnt_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -200.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -200.0 && data[this.currentlayer2] < 0.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 0.0 && data[this.currentlayer2] < 200.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 200.0 && data[this.currentlayer2] < 400.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 400.0 && data[this.currentlayer2] < 600.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 600.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_dslpm_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -300.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -300.0 && data[this.currentlayer2] < 0.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 0.0 && data[this.currentlayer2] < 280.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 280.0 && data[this.currentlayer2] < 580.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 580.0 && data[this.currentlayer2] < 850.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 850.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_cancr_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -45000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -45000.0 && data[this.currentlayer2] < -20000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -20000.0 && data[this.currentlayer2] < 5000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 5000.0 && data[this.currentlayer2] < 30000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 30000.0 && data[this.currentlayer2] < 55000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 55000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_resp_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -600.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -600.0 && data[this.currentlayer2] < -250) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -250.0 && data[this.currentlayer2] < 100.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 100.0 && data[this.currentlayer2] < 450.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 450.0 && data[this.currentlayer2] < 800.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 800.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_ptraf_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < 800000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 800000.0 && data[this.currentlayer2] < 1700000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 1700000.0 && data[this.currentlayer2] < 1700000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 2600000.0 && data[this.currentlayer2] < 2600000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 3500000.0 && data[this.currentlayer2] < 4400000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 4400000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_pwdis_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -47000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -47000.0 && data[this.currentlayer2] < -35000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -35000.0 && data[this.currentlayer2] < -22000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -22000.0 && data[this.currentlayer2] < -10000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -10000.0 && data[this.currentlayer2] < 200.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 200.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_pnpl_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -400.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -400.0 && data[this.currentlayer2] < -120.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -120.0 && data[this.currentlayer2] < 150.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 150.0 && data[this.currentlayer2] < 420.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 420.0 && data[this.currentlayer2] < 690.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 690.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_prmp_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -450.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -450.0 && data[this.currentlayer2] < 1000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 1000.0 && data[this.currentlayer2] < 2450.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 2450.0 && data[this.currentlayer2] < 3900.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 3900.0 && data[this.currentlayer2] < 5350.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 5350.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_ptsdf_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -3200.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -3200.0 && data[this.currentlayer2] < -1000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -1000.0 && data[this.currentlayer2] < 1800.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 1800.0 && data[this.currentlayer2] < 4600.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 4600.0 && data[this.currentlayer2] < 7300.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 7300.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_ozone_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -58000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -58000.0 && data[this.currentlayer2] < -28000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -28000.0 && data[this.currentlayer2] < 600.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 600.0 && data[this.currentlayer2] < 38000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 38000.0 && data[this.currentlayer2] < 70000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 70000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_pm25_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -11000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -11000.0 && data[this.currentlayer2] < -5500.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -5500.0 && data[this.currentlayer2] < 1000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 1000.0 && data[this.currentlayer2] < 7500.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 7500.0 && data[this.currentlayer2] < 15000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 15000.0) {
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

        ]
      }
    },
    getcovid19Style2: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer2 === 'cases') {
          if (data[this.currentlayer2] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < 1328) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer2] >= 1328 && data[this.currentlayer2] < 2656) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 2656 && data[this.currentlayer2] < 3984) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 3984 && data[this.currentlayer2] < 5416) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 5416 && data[this.currentlayer2] < 6644) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 6644) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer2 === 'cases_per_10000_res') {
          if (data[this.currentlayer2] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < 586.0) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer2] >= 586.0 && data[this.currentlayer2] < 1172.0) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 1172.0 && data[this.currentlayer2] < 1758.0) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 1758.0 && data[this.currentlayer2] < 2344.0) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 2344.0 && data[this.currentlayer2] < 2930.0) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 2930.0) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer2 === 'cases_per_100000_res') {
          if (data[this.currentlayer2] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < 5859.0) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer2] >= 5859.0 && data[this.currentlayer2] < 11718.0) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 11718.0 && data[this.currentlayer2] < 17577.0) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 17577.0 && data[this.currentlayer2] < 23436.0) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 23436.0 && data[this.currentlayer2] < 29295.0) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 29295.0) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer2 === 'deaths') {
          if (data[this.currentlayer2] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < 17) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer2] >= 17 && data[this.currentlayer2] < 34) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 34 && data[this.currentlayer2] < 51) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 51 && data[this.currentlayer2] < 65) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 65 && data[this.currentlayer2] < 85) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 85) {
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

        ]
      }
    },
    getncwellwiseLeadMaxStyle: function () {
      let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO

      function getPattern (color1) {
        canvas.width = 8 * pixelRatio
        canvas.height = 8 * pixelRatio
        let color2 = 'rgb(0, 0, 0, 0.0)'
        let numberOfStripes = 50
        for (var i = 0; i < numberOfStripes; i++) {
          var thickness = 200 / numberOfStripes
          context.beginPath()
          context.strokeStyle = i % 2 ? color1 : color2
          context.lineWidth = thickness
          context.lineCap = 'round'

          context.moveTo(0, i * thickness + thickness / 2)
          context.lineTo(300, i * thickness + thickness / 2)
          context.stroke()
        }
        return context.createPattern(canvas, 'repeat')
      }

      return feature => {
        let data = feature.getProperties()
        let color
        if (data.lead_maximum === -999.99) {
          color = 'rgba(50, 110, 219, 1.0)'
        } else if (data.lead_maximum < 11.0) {
          color = getPattern('rgba(196, 200, 207, 1.0)')
        } else if (data.lead_maximum >= 11.0 && data.lead_maximum < 30.0) {
          color = getPattern('rgba(156, 162, 173, 1.0)')
        } else if (data.lead_maximum >= 30.0 && data.lead_maximum < 50.0) {
          color = getPattern('rgba(116, 121, 130, 1.0)')
        } else if (data.lead_maximum >= 50.0 && data.lead_maximum < 80.0) {
          color = getPattern('rgba(79, 82, 89, 1.0)')
        } else if (data.lead_maximum >= 80.0 && data.lead_maximum < 100.0) {
          color = getPattern('rgba(55, 58, 64, 1.0)')
        } else if (data.lead_maximum >= 100.0) {
          color = getPattern('rgba(39, 40, 43, 1.0)')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: '#000',
              width: (this.zoom / 8.0),
              lineCap: 'round',
              lineJoin: 'bevel'
            }),
            fill: new Fill({
              color: color
            })
          })
        ]
      }
    },
    getncwellwiseMngMaxStyle: function () {
      let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO

      function getPattern (color2) {
        canvas.width = 8 * pixelRatio
        canvas.height = 8 * pixelRatio
        let color1 = 'rgb(0, 0, 0, 0.0)'
        let numberOfStripes = 50
        for (var i = 0; i < numberOfStripes; i++) {
          var thickness = 200 / numberOfStripes
          context.beginPath()
          context.strokeStyle = i % 2 ? color1 : color2
          context.lineWidth = thickness
          context.lineCap = 'round'

          context.moveTo(0, i * thickness + thickness / 2)
          context.lineTo(300, i * thickness + thickness / 2)
          context.stroke()
        }
        return context.createPattern(canvas, 'repeat')
      }
      return feature => {
        let data = feature.getProperties()
        let color
        if (data.manganese_maximum === -999.99) {
          color = 'rgba(91, 95, 99, 1.0)'
        } else if (data.manganese_maximum < 2800.0) {
          color = getPattern('rgba(194, 232, 190, 1.0)')
        } else if (data.manganese_maximum >= 2800.0 && data.manganese_maximum < 5800.0) {
          color = getPattern('rgba(81, 222, 67, 1.0)')
        } else if (data.manganese_maximum >= 5800.0 && data.manganese_maximum < 10800.0) {
          color = getPattern('rgba(25, 128, 11, 1.0)')
        } else if (data.manganese_maximum >= 10800.0 && data.manganese_maximum < 20800.0) {
          color = getPattern('rgba(14, 82, 5, 1.0)')
        } else if (data.manganese_maximum >= 20800.0 && data.manganese_maximum < 40800.0) {
          color = getPattern('rgba(30, 138, 114, 1.0)')
        } else if (data.manganese_maximum >= 40800.0) {
          color = getPattern('rgba(5, 97, 76, 1.0)')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: '#000',
              width: (this.zoom / 8.0),
              lineCap: 'round',
              lineJoin: 'bevel'
            }),
            fill: new Fill({
              color: color
            })
          })
        ]
      }
    },
    getNCWellwiseLayer1ID: function () {
      return 'ncwellwise_layer1'
    },
    getLTDBCensusLayer1ID: function () {
      return 'ltdb_census_layer1'
    },
    getEJScreenLayer1ID: function () {
      return 'ejscreen_layer1'
    },
    getCovid19Layer1ID: function () {
      return 'covid19_layer1'
    },
    getNCWellwiseLayer2ID: function () {
      return 'ncwellwise_layer2'
    },
    getLTDBCensusLayer2ID: function () {
      return 'ltdb_census_layer2'
    },
    getEJScreenLayer2ID: function () {
      return 'ejscreen_layer2'
    },
    getCovid19Layer2ID: function () {
      return 'covid19_layer2'
    },
    onMapMounted: function (map1) {
      // now ol.Map instance is ready and we can work with it directly
      this.$refs.map1.$map.getControls().extend([
        new Zoom({
          target: 'Zoom1Target'
        }),
        new ScaleLine({
          target: 'Scale1Target'
        }),
        new OverviewMap({
          collapsed: false,
          collapsible: true,
          target: 'OverviewMap1Target'
        }),
        new Attribution({
          collapsed: false,
          collapsible: false,
          target: 'Attribution1Target'
        })
      ])
      this.$refs.map2.$map.getControls().extend([
        /* new Zoom({
          target: 'Zoom2Target'
        }),
        new ScaleLine({
          target: 'Scale2Target'
        }),
        new OverviewMap({
          collapsed: false,
          collapsible: true,
          target: 'OverviewMap2Target'
        }),
        new Attribution({
          collapsed: false,
          collapsible: false,
          target: 'Attribution2Target'
        }) */
      ])
    },
    closeBarChart: function () {
      this.selectedFeature = this.selectedFeature.filter(f => f.id === 0)
      let drawFeatures = this.$refs.drawSource.getFeatures()
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
    showMap1PanelLayer: function () {
      let layer = this.layers1.find(layer => layer.visible)
      if (layer != null) {
        layer.visible = false
      }

      if (this.currentlayer1 === 'ncwellwise_arsenic_max') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        this.$refs.layer1Style[0].refresh()
      } else if (this.currentlayer1 === 'ncwellwise_cadmium_max') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        this.$refs.layer1Style[0].refresh()
      } else if (this.currentlayer1 === 'ncwellwise_lead_max') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        this.$refs.layer1Style[0].refresh()
      } else if (this.currentlayer1 === 'ncwellwise_mng_max') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        this.$refs.layer1Style[0].refresh()
      } else if (this.currentlayer1 === 'pnhwht12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'pnhblk12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'phisp12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'pasian12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'pntv12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'hincw12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'hincb12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'hinch12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'hinca12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'pwpov12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'pbpov12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'phpov12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'papov12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'pnapov12') {
        layer = this.layers1.find(layer => layer.id === 'ltdb_census_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_ldpnt_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_dslpm_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_cancr_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_resp_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_ptraf_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_pwdis_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_pnpl_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_prmp_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_ptsdf_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_ozone_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_pm25_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'cases') {
        layer = this.layers1.find(layer => layer.id === 'covid19_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'cases_per_10000_res') {
        layer = this.layers1.find(layer => layer.id === 'covid19_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'cases_per_100000_res') {
        layer = this.layers1.find(layer => layer.id === 'covid19_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'deaths') {
        layer = this.layers1.find(layer => layer.id === 'covid19_layer1')
        this.$refs.layer1Style[0].refresh()
        // this.$refs.layer1Style.refresh()
      }

      if (layer != null) {
        layer.visible = true
      }

      let alayer = this.layers1[4]
      if (this.triwellwiseArsenicMax1Model === 'Selected') {
        alayer.visible = true
      } else if (this.triwellwiseArsenicMax1Model === 'Not Selected') {
        alayer.visible = false
      }
      let clayer = this.layers1[5]
      if (this.triwellwiseCadmiumMax1Model === 'Selected') {
        clayer.visible = true
      } else if (this.triwellwiseCadmiumMax1Model === 'Not Selected') {
        clayer.visible = false
      }
    },
    showMap2PanelLayer: function () {
      let layer = this.layers2.find(layer => layer.visible)
      if (layer != null) {
        layer.visible = false
      }

      if (this.currentlayer2 === 'ncwellwise_arsenic_max') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        this.$refs.layer2Style[0].refresh()
      } else if (this.currentlayer2 === 'ncwellwise_cadmium_max') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        this.$refs.layer2Style[0].refresh()
      } else if (this.currentlayer2 === 'ncwellwise_lead_max') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        this.$refs.layer2Style[0].refresh()
      } else if (this.currentlayer2 === 'ncwellwise_mng_max') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        this.$refs.layer2Style[0].refresh()
      } else if (this.currentlayer2 === 'pnhwht12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'pnhblk12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'phisp12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'pasian12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'pntv12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'hincw12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'hincb12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'hinch12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'hinca12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'pwpov12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'pbpov12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'phpov12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'papov12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'pnapov12') {
        layer = this.layers2.find(layer => layer.id === 'ltdb_census_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_ldpnt_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_dslpm_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_cancr_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_resp_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_ptraf_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_pwdis_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_pnpl_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_prmp_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_ptsdf_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_ozone_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_pm25_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'cases') {
        layer = this.layers2.find(layer => layer.id === 'covid19_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'cases_per_10000_res') {
        layer = this.layers2.find(layer => layer.id === 'covid19_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'cases_per_100000_res') {
        layer = this.layers2.find(layer => layer.id === 'covid19_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'deaths') {
        layer = this.layers2.find(layer => layer.id === 'covid19_layer2')
        this.$refs.layer2Style[0].refresh()
        // this.$refs.layer2Style.refresh()
      }

      if (layer != null) {
        layer.visible = true
      }

      let llayer = this.layers2[4]
      if (this.triwellwiseLeadMax2Model === 'Selected') {
        llayer.visible = true
      } else if (this.triwellwiseLeadMax2Model === 'Not Selected') {
        llayer.visible = false
      }
      let mlayer = this.layers2[5]
      if (this.triwellwiseManganeseMax2Model === 'Selected') {
        mlayer.visible = true
      } else if (this.triwellwiseManganeseMax2Model === 'Not Selected') {
        mlayer.visible = false
      }
    },
    onMapClick: function (event) {
      let pixel = event.pixel
      let features = this.$refs.map1.$map.getFeaturesAtPixel(pixel)
      let layer1 = this.layers1.find(layer1 => layer1.visible)
      let layer2 = this.layers2.find(layer2 => layer2.visible)
      if (!features) {
        this.selectedFeatureMaxBarBox = []
        this.selectedFeatureAvgBarBox = []
        this.selectedFeatureMinBarBox = []
        this.selectedFeatureStdBarBox = []
        this.selectedFeature = []
      } else if (features) {
        if (layer1.id === 'ncwellwise_layer1' || layer2.id === 'ncwellwise_layer2') {
          this.selectedFeatureMaxBarBox = []
          this.selectedFeatureAvgBarBox = []
          this.selectedFeatureMinBarBox = []
          this.selectedFeatureStdBarBox = []
          this.eventCoordinate = event.coordinate
          let feature = features[0]
          let properties = feature.getProperties()
          if (properties['geoid10']) {
            this.pid = properties['geoid10']
            this.selectedFeatureMaxBarBox.push(properties['arsenic_maximum'])
            this.selectedFeatureMaxBarBox.push(properties['cadmium_maximum'])
            this.selectedFeatureMaxBarBox.push(properties['lead_maximum'])
            this.selectedFeatureMaxBarBox.push(properties['manganese_maximum'])
            this.selectedFeatureAvgBarBox.push(properties['arsenic_mean'])
            this.selectedFeatureAvgBarBox.push(properties['cadmium_mean'])
            this.selectedFeatureAvgBarBox.push(properties['lead_mean'])
            this.selectedFeatureAvgBarBox.push(properties['manganese_mean'])
            this.selectedFeatureMinBarBox.push(properties['arsenic_minimum'])
            this.selectedFeatureMinBarBox.push(properties['cadmium_minimum'])
            this.selectedFeatureMinBarBox.push(properties['lead_minimum'])
            this.selectedFeatureMinBarBox.push(properties['manganese_minimum'])
            this.selectedFeatureStdBarBox.push(properties['arsenic_std'])
            this.selectedFeatureStdBarBox.push(properties['cadmium_std'])
            this.selectedFeatureStdBarBox.push(properties['lead_std'])
            this.selectedFeatureStdBarBox.push(properties['manganese_std'])
          }
        }
      }
    } /* ,
    onUpdatePosition: function (coordinate) {
      // console.log(coordinate)
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
  .dualmap {
    margin: 0;
    padding: 1px;
    width: 50%;
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
    background-color: rgba(119, 52, 235, 0.65);
    display: inline-block;
  }
  .assqu2 {
    height: 25px;
    width: 25px;
    background-color: rgba(143, 52, 235, 0.65);
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
    background-color: rgba(186, 52, 235, 0.65);
    display: inline-block;
  }
  .assqu5 {
    height: 25px;
    width: 25px;
    background-color: rgba(211, 52, 235, 0.65);
    display: inline-block;
  }
  .assqu6 {
    height: 25px;
    width: 25px;
    background-color: rgba(235, 52, 220, 0.65);
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
