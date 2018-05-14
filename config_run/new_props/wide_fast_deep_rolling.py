import lsst.pex.config as pexConfig
from lsst.sims.ocs.configuration.proposal import General, GeneralBandFilter, Selection, SelectionList, TimeRange
from lsst.sims.ocs.configuration.proposal import general_prop_reg
__all__ = ["WideFastDeepRolling"]
@pexConfig.registerConfig("WideFastDeepRolling", general_prop_reg, General)
class WideFastDeepRolling(General):
    def setDefaults(self):
        self.name = "WideFastDeepRolling"
        # -------------------------
        # Sky Region specifications
        # -------------------------
        sel0 = Selection()
        sel0.limit_type = "Dec"
        sel0.minimum_limit = -62.5
        sel0.maximum_limit = -24.7
        sel1 = Selection()
        sel1.limit_type = "Dec"
        sel1.minimum_limit = -24.7
        sel1.maximum_limit = 2.8
        sel2 = Selection()
        sel2.limit_type = "Dec"
        sel2.minimum_limit = -62.5
        sel2.maximum_limit = -24.7
        sel3 = Selection()
        sel3.limit_type = "Dec"
        sel3.minimum_limit = -24.7
        sel3.maximum_limit = 2.8
        sel4 = Selection()
        sel4.limit_type = "Dec"
        sel4.minimum_limit = -62.5
        sel4.maximum_limit = -24.7
        sel5 = Selection()
        sel5.limit_type = "Dec"
        sel5.minimum_limit = -24.7
        sel5.maximum_limit = 2.8
        sel6 = Selection()
        sel6.limit_type = "Dec"
        sel6.minimum_limit = -62.5
        sel6.maximum_limit = -24.7
        sel7 = Selection()
        sel7.limit_type = "Dec"
        sel7.minimum_limit = -24.7
        sel7.maximum_limit = 2.8
        sel8 = Selection()
        sel8.limit_type = "Dec"
        sel8.minimum_limit = -62.5
        sel8.maximum_limit = -24.7
        sel9 = Selection()
        sel9.limit_type = "Dec"
        sel9.minimum_limit = -24.7
        sel9.maximum_limit = 2.8
        self.sky_region.selections = {0: sel0,
                                      1: sel1,
                                      2: sel2,
                                      3: sel3,
                                      4: sel4,
                                      5: sel5,
                                      6: sel6,
                                      7: sel7,
                                      8: sel8,
                                      9: sel9}
        time_range0 = TimeRange()
        time_range0.start = 1
        time_range0.end = 365
        time_range1 = TimeRange()
        time_range1.start = 366
        time_range1.end = 730
        time_range2 = TimeRange()
        time_range2.start = 731
        time_range2.end = 1095
        time_range3 = TimeRange()
        time_range3.start = 1096
        time_range3.end = 1460
        time_range4 = TimeRange()
        time_range4.start = 1461
        time_range4.end = 1825
        time_range5 = TimeRange()
        time_range5.start = 1826
        time_range5.end = 2190
        time_range6 = TimeRange()
        time_range6.start = 2191
        time_range6.end = 2555
        time_range7 = TimeRange()
        time_range7.start = 2556
        time_range7.end = 2920
        time_range8 = TimeRange()
        time_range8.start = 2921
        time_range8.end = 3285
        time_range9 = TimeRange()
        time_range9.start = 3286
        time_range9.end = 3650
        self.sky_region.time_ranges = {0: time_range0,
                                       1: time_range1,
                                       2: time_range2,
                                       3: time_range3,
                                       4: time_range4,
                                       5: time_range5,
                                       6: time_range6,
                                       7: time_range7,
                                       8: time_range8,
                                       9: time_range9}
        sel_map0 = SelectionList()
        sel_map0.indexes = [0]
        sel_map1 = SelectionList()
        sel_map1.indexes = [1]
        sel_map2 = SelectionList()
        sel_map2.indexes = [2]
        sel_map3 = SelectionList()
        sel_map3.indexes = [3]
        sel_map4 = SelectionList()
        sel_map4.indexes = [4]
        sel_map5 = SelectionList()
        sel_map5.indexes = [5]
        sel_map6 = SelectionList()
        sel_map6.indexes = [6]
        sel_map7 = SelectionList()
        sel_map7.indexes = [7]
        sel_map8 = SelectionList()
        sel_map8.indexes = [8]
        sel_map9 = SelectionList()
        sel_map9.indexes = [9]
        self.sky_region.selection_mapping = {0: sel_map0,
                                             1: sel_map1,
                                             2: sel_map2,
                                             3: sel_map3,
                                             4: sel_map4,
                                             5: sel_map5,
                                             6: sel_map6,
                                             7: sel_map7,
                                             8: sel_map8,
                                             9: sel_map9}
        # ----------------------------
        # Sky Exclusion specifications
        # ----------------------------
        self.sky_exclusion.dec_window = 90.0
        excl0 = Selection()
        excl0.limit_type = "GP"
        excl0.minimum_limit = 0.0
        excl0.maximum_limit = 10.0
        excl0.bounds_limit = 90.0
        self.sky_exclusion.selections = {0: excl0}
        # ---------------------------------
        # Sky Nightly Bounds specifications
        # ---------------------------------
        self.sky_nightly_bounds.twilight_boundary = -12.0
        self.sky_nightly_bounds.delta_lst = 60.0
        # ------------------------------
        # Sky Constraints specifications
        # ------------------------------
        self.sky_constraints.max_airmass = 1.5
        self.sky_constraints.max_cloud = 0.7
        # ----------------------
        # Scheduling information
        # ----------------------
        self.scheduling.max_num_targets = 500
        self.scheduling.accept_serendipity = False
        self.scheduling.accept_consecutive_visits = False
        self.scheduling.restrict_grouped_visits = True
        self.scheduling.time_interval = 1800
        self.scheduling.time_window_start = .5
        self.scheduling.time_window_max = 1.0
        self.scheduling.time_window_end = 2.0
        self.scheduling.time_weight = 1.0
        self.sky_constraints.max_cloud = 0.7
        # ----------------
        # HA and X bonuses
        # ----------------
        self.scheduling.airmass_bonus=0.0
        self.scheduling.hour_angle_bonus=0.3
        self.scheduling.hour_angle_max=3.0
        # --------------------------
        # Band Filter specifications
        # --------------------------
        u_filter = GeneralBandFilter()
        u_filter.name = 'u'
        u_filter.num_visits = 75
        u_filter.num_grouped_visits = 1
        u_filter.bright_limit = 21.3
        u_filter.dark_limit = 30.0
        u_filter.max_seeing = 1.5
        u_filter.exposures = [15.0, 15.0]
        g_filter = GeneralBandFilter()
        g_filter.name = 'g'
        g_filter.num_visits = 105
        g_filter.num_grouped_visits = 2
        g_filter.bright_limit = 21.0
        g_filter.dark_limit = 30.0
        g_filter.max_seeing = 1.5
        g_filter.exposures = [15.0, 15.0]
        r_filter = GeneralBandFilter()
        r_filter.name = 'r'
        r_filter.num_visits = 240
        r_filter.num_grouped_visits = 2
        r_filter.bright_limit = 20.25
        r_filter.dark_limit = 30.0
        r_filter.max_seeing = 1.5
        r_filter.exposures = [15.0, 15.0]
        i_filter = GeneralBandFilter()
        i_filter.name = 'i'
        i_filter.num_visits = 240
        i_filter.num_grouped_visits = 2
        i_filter.bright_limit = 19.5
        i_filter.dark_limit = 30.0
        i_filter.max_seeing = 1.5
        i_filter.exposures = [15.0, 15.0]
        z_filter = GeneralBandFilter()
        z_filter.name = 'z'
        z_filter.num_visits = 210
        z_filter.num_grouped_visits = 2
        z_filter.bright_limit = 17.0
        z_filter.dark_limit = 21.0
        z_filter.max_seeing = 1.5
        z_filter.exposures = [15.0, 15.0]
        y_filter = GeneralBandFilter()
        y_filter.name = 'y'
        y_filter.num_visits = 210
        y_filter.num_grouped_visits = 1
        y_filter.bright_limit = 16.5
        y_filter.dark_limit = 21.0
        y_filter.max_seeing = 1.5
        y_filter.exposures = [15.0, 15.0]
        self.filters = {u_filter.name: u_filter,
                        g_filter.name: g_filter,
                        r_filter.name: r_filter,
                        i_filter.name: i_filter,
                        z_filter.name: z_filter,
                        y_filter.name: y_filter}