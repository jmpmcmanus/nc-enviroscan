<template>
  <q-layout view="lhr lpr lfr">
    <!--// Left Drawer -->
    <q-drawer v-model="leftDrawerOpen" show-if-above bordered :content-style="{ backgroundColor: 'rgba(199, 235, 235, 0.5)' }">
      <q-space />
      <q-separator />
      <q-space />
      <q-card class="q-pa-md bg-teal-1" style="max-width: 300px">
        <table class="table is-fullwidth">
          <div v-if="Object.keys(selectedFeaturesAvgBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxavgoptions" :series="selectedFeaturesAvgBarBox"></apexchart>
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
          <div v-if="Object.keys(selectedFeaturesMinBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxminoptions" :series="selectedFeaturesMinBarBox"></apexchart>
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
          <div v-if="Object.keys(selectedFeaturesStdBarBox).length > 0">
            <tr>
              <td>
                <apexchart width="280" type="radialBar" :options="apxstdoptions" :series="selectedFeaturesStdBarBox"></apexchart>
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

        <!-- // map 1 layers -->
        <q-expansion-item default-opened expand-separator icon="list" label="Top Map Layers">
          <div class="q-pa-md q-gutter-y-sm column">
            <q-toggle
              :label="`Arsenic Maximum Layer ${ ncwellwiseArsenicMax1Model }`"
              :key="layers1[0].id"
              v-on:input="showMap1PanelLayer(layers)"
              :class="{ 'is-active': layers1[0].visible }"
              color="teal"
              false-value="Not Selected"
              true-value="Selected"
              v-model="ncwellwiseArsenicMax1Model"
            />
            <q-toggle
              :label="`Cadmium Maximum Layer ${ ncwellwiseCadmiumMax1Model }`"
              :key="layers1[1].id"
              v-on:input="showMap1PanelLayer(layers)"
              :class="{ 'is-active': layers1[1].visible }"
              color="teal"
              false-value="Not Selected"
              true-value="Selected"
              v-model="ncwellwiseCadmiumMax1Model"
            />
            <q-toggle
              :label="`Lead Maximum Layer ${ ncwellwiseLeadMax1Model }`"
              :key="layers1[2].id"
              v-on:input="showMap1PanelLayer(layers)"
              :class="{ 'is-active': layers1[2].visible }"
              color="teal"
              false-value="Not Selected"
              true-value="Selected"
              v-model="ncwellwiseLeadMax1Model"
            />
            <q-toggle
              :label="`Manganese Maximum Layer ${ ncwellwiseMngMax1Model }`"
              :key="layers1[3].id"
              v-on:input="showMap1PanelLayer(layers)"
              :class="{ 'is-active': layers1[3].visible }"
              color="teal"
              false-value="Not Selected"
              true-value="Selected"
              v-model="ncwellwiseMngMax1Model"
            />
          </div>
        </q-expansion-item>
        <!-- // map 1 layers -->

        <!-- // map 2 layers -->
        <q-expansion-item default-opened expand-separator icon="list" label="Bottom Map Layers">
          <div class="q-pa-md q-gutter-y-sm column">
            <q-toggle
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
            />
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
                  <q-expansion-item expand-separator icon="list" label="Arsenic Maximum (ppm)">
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
                  <q-expansion-item expand-separator icon="list" label="Cadmium Maximum (ppm)">
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
                  <q-expansion-item expand-separator icon="list" label="Lead Maximum (ppm)">
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
                  <q-expansion-item expand-separator icon="list" label="Maganese Maximum (ppm)">
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
        <vl-interaction-select ref="selectInteraction" :features.sync="selectedFeatures">
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
                      <q-btn flat round dense icon="close" @click="selectedFeatures = selectedFeatures.filter(f => f.id !== feature.id)" />
                    </template>
                  </q-banner>
                  <table class="table is-fullwidth">
                    <div v-if="Object.keys(selectedFeaturesMaxBarBox).length > 0">
                    <tr>
                      <td>
                        <apexchart width="400" type="radialBar" :options="apxmaxoptions" :series="selectedFeaturesMaxBarBox"></apexchart>
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
          <component :is="'vl-source-' + layer.name" v-bind="layer"></component>
        </vl-layer-tile>
        <!--// base layers -->

        <!--// other layers1 from config -->
        <!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
        <component v-for="layer in layers1" :is="layer.cmp" v-if="layer.visible" :key="layer.id" v-bind="layer">
          <!--// add vl-source-* -->
          <component ref="layer1Source" :is="layer.source.cmp" v-bind="layer.source">
          </component>

          <!--// add style components if provided -->
          <!--// create vl-style-box or vl-style-func -->
          <component v-if="layer.style" v-for="(style, i) in layer.style" :key="i" :is="style.cmp" v-bind="style">
          </component>
        </component>
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
        <vl-interaction-select ref="selectInteraction" :features.sync="selectedFeatures">
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
                      <q-btn flat round dense icon="close" @click="selectedFeatures = selectedFeatures.filter(f => f.id !== feature.id)" />
                    </template>
                  </q-banner>
                  <table class="table is-fullwidth">
                    <div v-if="Object.keys(selectedFeaturesMaxBarBox).length > 0">
                    <tr>
                      <td>
                        <apexchart width="400" type="radialBar" :options="apxmaxoptions" :series="selectedFeaturesMaxBarBox"></apexchart>
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
          <component v-if="layer.style" v-for="(style, i) in layer.style" :key="i" :is="style.cmp" v-bind="style">
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
      <div id="ZoomTarget"></div>
    </q-page-sticky>
    <q-page-sticky position="bottom-left" :offset="[8, 38]">
      <div id="OverviewMapTarget"></div>
    </q-page-sticky>
    <q-page-sticky position="bottom-left" :offset="[15, 8]">
      <div id="ScaleTarget"></div>
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
import { findPointOnSurface } from 'vuelayers/lib/ol-ext'
import { camelCase } from 'lodash'

// ol controls import
import ScaleLine from 'ol/control/ScaleLine'
import OverviewMap from 'ol/control/OverviewMap'
import Zoom from 'ol/control/Zoom'
import Attribution from 'ol/control/Attribution'

// other ol imports
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
          text: 'Multiple Radial Bars',
          align: 'left',
          style: {
            color: '#FFF'
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
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppm'
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
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppm'
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
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppm'
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
            return seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex] + ' ppm'
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
      zoom: 12,
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
      ncwellwiseArsenicMax1Model: 'Selected',
      ncwellwiseCadmiumMax1Model: 'Not Selected',
      ncwellwiseLeadMax1Model: 'Not Selected',
      ncwellwiseMngMax1Model: 'Not Selected',
      ncwellwiseArsenicMax2Model: 'Selected',
      ncwellwiseCadmiumMax2Model: 'Not Selected',
      ncwellwiseLeadMax2Model: 'Not Selected',
      ncwellwiseMngMax2Model: 'Not Selected',
      ttitle: undefined,
      // stored and selected features
      storeFeatures: [],
      selectedFeatures: [],
      selectedFeaturesMaxBarBox: [],
      selectedFeaturesAvgBarBox: [],
      selectedFeaturesMinBarBox: [],
      selectedFeaturesStdBarBox: [],
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
      primelayer1: 'ncwellwise_arsenic_max',
      primelayer2: 'ncwellwise_arsenic_max', // 'ncwellwise_arsenic_max',
      layers1: [
        {
          id: 'ncwellwise_arsenic_max',
          title: 'NC wellwise Arsenic Maximum',
          cmp: 'vl-layer-vector',
          visible: true,
          source: {
            cmp: 'vl-source-vector',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_subset_20102019_geom/?format=json'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseArsenicMaxStyle
            }
          ]
        },
        {
          id: 'ncwellwise_cadmium_max',
          title: 'NC Wellwise Cadmium Maximum',
          cmp: 'vl-layer-vector',
          visible: false,
          source: {
            cmp: 'vl-source-vector',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_subset_20102019_geom/?format=json'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseCadmiumMaxStyle
            }
          ]
        },
        {
          id: 'ncwellwise_lead_max',
          title: 'NC wellwise Lead Maximum',
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
          id: 'ncwellwise_mng_max',
          title: 'NC Wellwise Manganese Maximum',
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
      ],
      layers2: [
        {
          id: 'ncwellwise_arsenic_max',
          title: 'NC wellwise Arsenic Maximum',
          cmp: 'vl-layer-vector',
          visible: true,
          source: {
            cmp: 'vl-source-vector',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_subset_20102019_geom/?format=json'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseArsenicMaxStyle
            }
          ]
        },
        {
          id: 'ncwellwise_cadmium_max',
          title: 'NC Wellwise Cadmium Maximum',
          cmp: 'vl-layer-vector',
          visible: false,
          source: {
            cmp: 'vl-source-vector',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_subset_20102019_geom/?format=json'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseCadmiumMaxStyle
            }
          ]
        },
        {
          id: 'ncwellwise_lead_max',
          title: 'NC wellwise Lead Maximum',
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
          id: 'ncwellwise_mng_max',
          title: 'NC Wellwise Manganese Maximum',
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
    getncwellwiseArsenicMaxStyle: function () {
      let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO

      function getPattern (color1) {
        canvas.width = 8 * pixelRatio
        canvas.height = 8 * pixelRatio
        let color2 = 'rgb(0, 0, 0, 0.0)'
        let numberOfStripes = 50
        for (var i = 0; i < numberOfStripes * 2; i++) {
          var thickness = 200 / numberOfStripes
          context.beginPath()
          context.strokeStyle = i % 2 ? color1 : color2
          context.lineWidth = thickness
          context.lineCap = 'round'

          context.moveTo(i * thickness * pixelRatio + thickness / 2 - 300, 0)
          context.lineTo(0 + i * thickness * pixelRatio + thickness / 2, 300)
          context.stroke()
        }
        return context.createPattern(canvas, 'repeat')
      }
      return feature => {
        let data = feature.getProperties()
        let color
        if (data.arsenic_maximum === -999.99) {
          color = 'rgba(91, 95, 99, 0.65)'
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
          color = 'rgba(91, 95, 99, 0.65)'
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
    getncwellwiseLeadMaxStyle: function () {
      let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO

      function getPattern (color1) {
        canvas.width = 8 * pixelRatio
        canvas.height = 8 * pixelRatio
        let color2 = 'rgb(0, 0, 0, 0.0)'
        let numberOfStripes = 50
        for (var i = 0; i < numberOfStripes * 2; i++) {
          var thickness = 200 / numberOfStripes
          context.beginPath()
          context.strokeStyle = i % 2 ? color1 : color2
          context.lineWidth = thickness
          context.lineCap = 'round'

          context.moveTo(i * thickness * pixelRatio + thickness / 2 - 300, 300)
          context.lineTo(0 + i * thickness * pixelRatio + thickness / 2, 0)
          context.stroke()
        }
        return context.createPattern(canvas, 'repeat')
      }

      return feature => {
        let data = feature.getProperties()
        let color
        if (data.lead_maximum === -999.99) {
          color = 'rgba(50, 110, 219, 0.65)'
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
        if (data.manganese_maximum === -999.99) {
          color = 'rgba(91, 95, 99, 0.65)'
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
    onMapMounted: function (map1) {
      // now ol.Map instance is ready and we can work with it directly
      this.$refs.map1.$map.getControls().extend([
        new Zoom({
          target: 'ZoomTarget'
        })
      ])
      this.$refs.map2.$map.getControls().extend([
        new ScaleLine({
          target: 'ScaleTarget'
        }),
        new OverviewMap({
          collapsed: false,
          collapsible: true,
          target: 'OverviewMapTarget'
        }),
        new Attribution({
          collapsed: false,
          collapsible: false,
          target: 'AttributionTarget'
        })
      ])
    },
    closeBarChart: function () {
      this.selectedFeatures = this.selectedFeatures.filter(f => f.id === 0)
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
      let alayer = this.layers1[0]
      if (this.ncwellwiseArsenicMax1Model === 'Selected') {
        alayer.visible = true
      } else if (this.ncwellwiseArsenicMax1Model === 'Not Selected') {
        alayer.visible = false
      }
      let clayer = this.layers1[1]
      if (this.ncwellwiseCadmiumMax1Model === 'Selected') {
        clayer.visible = true
      } else if (this.ncwellwiseCadmiumMax1Model === 'Not Selected') {
        clayer.visible = false
      }
      let llayer = this.layers1[2]
      if (this.ncwellwiseLeadMax1Model === 'Selected') {
        llayer.visible = true
      } else if (this.ncwellwiseLeadMax1Model === 'Not Selected') {
        llayer.visible = false
      }
      let mlayer = this.layers1[3]
      if (this.ncwellwiseMngMax1Model === 'Selected') {
        mlayer.visible = true
      } else if (this.ncwellwiseMngMax1Model === 'Not Selected') {
        mlayer.visible = false
      }
    },
    showMap2PanelLayer: function () {
      let alayer = this.layers2[0]
      if (this.ncwellwiseArsenicMax2Model === 'Selected') {
        alayer.visible = true
      } else if (this.ncwellwiseArsenicMax2Model === 'Not Selected') {
        alayer.visible = false
      }
      let clayer = this.layers2[1]
      if (this.ncwellwiseCadmiumMax2Model === 'Selected') {
        clayer.visible = true
      } else if (this.ncwellwiseCadmiumMax2Model === 'Not Selected') {
        clayer.visible = false
      }
      let llayer = this.layers2[2]
      if (this.ncwellwiseLeadMax2Model === 'Selected') {
        llayer.visible = true
      } else if (this.ncwellwiseLeadMax2Model === 'Not Selected') {
        llayer.visible = false
      }
      let mlayer = this.layers2[3]
      if (this.ncwellwiseMngMax2Model === 'Selected') {
        mlayer.visible = true
      } else if (this.ncwellwiseMngMax2Model === 'Not Selected') {
        mlayer.visible = false
      }
    },
    onMapClick: function (event) {
      let pixel = event.pixel
      let features = this.$refs.map1.$map.getFeaturesAtPixel(pixel)

      if (!features) {
        this.selectedFeaturesMaxBarBox = []
        this.selectedFeaturesAvgBarBox = []
        this.selectedFeaturesMinBarBox = []
        this.selectedFeaturesStdBarBox = []
        this.selectedFeatures = []
      } else if (features) {
        this.selectedFeaturesMaxBarBox = []
        this.selectedFeaturesAvgBarBox = []
        this.selectedFeaturesMinBarBox = []
        this.selectedFeaturesStdBarBox = []
        this.eventCoordinate = event.coordinate
        let feature = features[0]
        if (feature.id_ !== undefined) {
          let properties = feature.getProperties()
          if (properties['geoid10']) {
            this.pid = properties['geoid10']
            this.selectedFeaturesMaxBarBox.push(properties['arsenic_maximum'])
            this.selectedFeaturesMaxBarBox.push(properties['cadmium_maximum'])
            this.selectedFeaturesMaxBarBox.push(properties['lead_maximum'])
            this.selectedFeaturesMaxBarBox.push(properties['manganese_maximum'])
            this.selectedFeaturesAvgBarBox.push(properties['arsenic_mean'])
            this.selectedFeaturesAvgBarBox.push(properties['cadmium_mean'])
            this.selectedFeaturesAvgBarBox.push(properties['lead_mean'])
            this.selectedFeaturesAvgBarBox.push(properties['manganese_mean'])
            this.selectedFeaturesMinBarBox.push(properties['arsenic_minimum'])
            this.selectedFeaturesMinBarBox.push(properties['cadmium_minimum'])
            this.selectedFeaturesMinBarBox.push(properties['lead_minimum'])
            this.selectedFeaturesMinBarBox.push(properties['manganese_minimum'])
            this.selectedFeaturesStdBarBox.push(properties['arsenic_std'])
            this.selectedFeaturesStdBarBox.push(properties['cadmium_std'])
            this.selectedFeaturesStdBarBox.push(properties['lead_std'])
            this.selectedFeaturesStdBarBox.push(properties['manganese_std'])
          }
        } else {
          // this.selectedFeaturesMaxBarBox = []
          // this.selectedFeaturesAvgBarBox = []
          // this.selectedFeaturesMinBarBox = []
          // this.selectedFeaturesStdBarBox = []
          // this.selectedFeatures = []
        }
      }
    },
    onUpdatePosition: function (coordinate) {
      // console.log(coordinate)
      this.deviceCoordinate = coordinate
      this.center = [this.deviceCoordinate[0], this.deviceCoordinate[1]]
    },
    onUpdateAccuracy: function (accuracy) {
      this.coordinateAccuracy = accuracy
    }
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
