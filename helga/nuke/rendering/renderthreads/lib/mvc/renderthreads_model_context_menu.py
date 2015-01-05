

"""
renderthreads_model_context_menu
==========================================

Menu created on right-click at renderthreads
model instance.

-----------------------

**Author:** `Timm Wagener <mailto:wagenertimm@gmail.com>`_
"""


# Import
# ------------------------------------------------------------------
# python
import sys
import os
import functools
import logging
# PySide
from PySide import QtGui
from PySide import QtCore


#  Import variable
do_reload = True


#  renderthreads

#  lib

#  renderthreads_globals
from .. import renderthreads_globals
if(do_reload):
    reload(renderthreads_globals)

#  renderthreads_logging
from .. import renderthreads_logging
if(do_reload):
    reload(renderthreads_logging)

#  renderthreads_nuke
from .. import renderthreads_nuke
if(do_reload):
    reload(renderthreads_nuke)

# lib.gui

# renderthreads_gui_helper
from ..gui import renderthreads_gui_helper
if(do_reload):
    reload(renderthreads_gui_helper)


# NodesContextMenu
# ------------------------------------------------------------------
class NodesContextMenu(QtGui.QMenu):
    """
    Customized context menu for the model
    that manages the renderthread nodes.
    """

    
    def __new__(cls, *args, **kwargs):
        """
        NodesContextMenu instance factory.
        """

        # nodes_context_menu_instance
        nodes_context_menu_instance = super(NodesContextMenu, cls).__new__(cls, args, kwargs)

        return nodes_context_menu_instance

    
    def __init__(self,
                dev=True,
                logging_level = logging.DEBUG,
                parent = None):
        """
        Customize instance.
        """

        # super and objectName
        # ------------------------------------------------------------------
        
        # parent_class
        self.parent_class = super(NodesContextMenu, self)
        self.parent_class.__init__(parent=parent)

        # setObjectName
        self.setObjectName(self.__class__.__name__)

        # instance variables
        # ------------------------------------------------------------------

        # dev
        self.dev = dev
        
        # logger
        self.logger = renderthreads_logging.get_logger(self.__class__.__name__)

        # view
        self.view = None
        
        # Init procedure
        # ------------------------------------------------------------------
        
        # setup_ui
        self.setup_ui()

        # connect_ui
        self.connect_ui()

        # style_ui
        self.style_ui()

        # run_tests
        self.run_tests()

    # Setup
    # ------------------------------------------------------------------
    
    def setup_ui(self):
        """
        Setup menu ui.
        """

        # acn_add_selected
        self.acn_add_selected = QtGui.QAction('Add selected write nodes', self)
        self.acn_add_selected.setObjectName(self.__class__.__name__ + '_' + 'acn_add_selected')
        self.addAction(self.acn_add_selected)

        # acn_add_all
        self.acn_add_all = QtGui.QAction('Add all write nodes', self)
        self.acn_add_all.setObjectName(self.__class__.__name__ + '_' + 'acn_add_all')
        self.addAction(self.acn_add_all)

        # Separator
        self.addSeparator()

        # mnu_remove
        self.mnu_remove = QtGui.QMenu('Remove', parent = self)
        self.mnu_remove.setObjectName(self.__class__.__name__ + '_' + 'mnu_remove')
        self.addMenu(self.mnu_remove)

        # acn_remove_selected
        self.acn_remove_selected = QtGui.QAction('Remove selected nodes', self)
        self.acn_remove_selected.setObjectName(self.__class__.__name__ + '_' + 'acn_remove_selected')
        self.mnu_remove.addAction(self.acn_remove_selected)

        # acn_remove_all
        self.acn_remove_all = QtGui.QAction('Remove all nodes', self)
        self.acn_remove_all.setObjectName(self.__class__.__name__ + '_' + 'acn_remove_all')
        self.mnu_remove.addAction(self.acn_remove_all)

        # Separator
        self.addSeparator()

        # mnu_select
        self.mnu_select = QtGui.QMenu('Select', parent = self)
        self.mnu_select.setObjectName(self.__class__.__name__ + '_' + 'mnu_select')
        self.addMenu(self.mnu_select)

        # acn_select_selected
        self.acn_select_selected = QtGui.QAction('Select selected nodes', self)
        self.acn_select_selected.setObjectName(self.__class__.__name__ + '_' + 'acn_select_selected')
        self.mnu_select.addAction(self.acn_select_selected)

        # acn_select_all
        self.acn_select_all = QtGui.QAction('Select all nodes', self)
        self.acn_select_all.setObjectName(self.__class__.__name__ + '_' + 'acn_select_all')
        self.mnu_select.addAction(self.acn_select_all)

        # Separator
        self.mnu_select.addSeparator()

        # acn_deselect_all
        self.acn_deselect_all = QtGui.QAction('Deselect all DAG nodes', self)
        self.acn_deselect_all.setObjectName(self.__class__.__name__ + '_' + 'acn_deselect_all')
        self.mnu_select.addAction(self.acn_deselect_all)

        # Separator
        self.addSeparator()

        # mnu_render
        self.mnu_render = QtGui.QMenu('Render', parent = self)
        self.mnu_render.setObjectName(self.__class__.__name__ + '_' + 'mnu_render')
        self.addMenu(self.mnu_render)

        # acn_render_selected
        self.acn_render_selected = QtGui.QAction('Render selected nodes', self)
        self.acn_render_selected.setObjectName(self.__class__.__name__ + '_' + 'acn_render_selected')
        self.mnu_render.addAction(self.acn_render_selected)

        # acn_render_all
        self.acn_render_all = QtGui.QAction('Render all nodes', self)
        self.acn_render_all.setObjectName(self.__class__.__name__ + '_' + 'acn_render_all')
        self.mnu_render.addAction(self.acn_render_all)

        # dev
        if (self.is_dev()):

            # Separator
            self.addSeparator()

            # mnu_dev
            self.mnu_dev = QtGui.QMenu('Dev', parent = self)
            self.mnu_dev.setObjectName(self.__class__.__name__ + '_' + 'mnu_dev')
            self.addMenu(self.mnu_dev)


    # Connect
    # ------------------------------------------------------------------

    def connect_ui(self):
        """
        Connect UI widgets with slots or functions.
        """

        # acn_add_selected
        self.acn_add_selected.triggered.connect(functools.partial(self.add_selected))
        # acn_add_all
        self.acn_add_all.triggered.connect(functools.partial(self.add_all))

        # acn_remove_selected
        self.acn_remove_selected.triggered.connect(functools.partial(self.remove_selected))
        # acn_remove_all
        self.acn_remove_all.triggered.connect(functools.partial(self.remove_all))

        # acn_select_selected
        self.acn_select_selected.triggered.connect(functools.partial(self.select_selected))
        # acn_select_all
        self.acn_select_all.triggered.connect(functools.partial(self.select_all))
        # acn_deselect_all
        self.acn_deselect_all.triggered.connect(functools.partial(self.deselect_all))

        # acn_render_selected
        self.acn_render_selected.triggered.connect(functools.partial(self.dummy_method, 'acn_render_selected'))
        # acn_render_all
        self.acn_render_all.triggered.connect(functools.partial(self.dummy_method, 'acn_render_all'))
        
    # Style
    # ------------------------------------------------------------------

    def style_ui(self):
        """
        Setup tool palette, tool stylesheet and specific widget stylesheets.
        """

        # styled_background
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Popup)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        # correct_styled_background_attribute
        renderthreads_gui_helper.correct_styled_background_attribute(self)

        # set_margins_and_spacing_for_child_layouts
        renderthreads_gui_helper.set_margins_and_spacing_for_child_layouts(self)

        # adjust size (Shrink to minimum size)
        # self.adjustSize()
    
    # Getter & Setter
    # ------------------------------------------------------------------

    def set_view_and_model(self, view):
        """
        Set self.view and self.model
        """

        self.view = view
        self.model = view.model()

    def is_dev(self):
        """
        Return developer status of app.
        """

        return self.dev

    # Methods
    # ------------------------------------------------------------------

    def get_selected_indices(self):
        """
        Return list of selected indices from view.
        """

        # if view
        if (self.view):
            # selected_indices_list
            selected_indices_list = self.view.selectedIndexes()
        # else
        else:
            # selected_indices_list
            selected_indices_list = []

        return selected_indices_list

    def indices_list_to_data_list(self, model_index_list):
        """
        Convert a list of modelindices to the list of
        data they contain. This does NOT give the renderthreads
        nodes from the models data list, but the content of
        the view fields.
        """

        try:
            # data_list
            data_list = [model_index.data() for model_index in model_index_list]

        except:
            # data_list
            data_list = []

        return data_list

    def indices_list_to_node_list(self, model_index_list):
        """
        Convert a list of modelindices to the list of
        renderthread nodes from the model.
        """

        # node_list
        node_list = []

        try:
            # iterate
            for index in model_index_list:

                # index invalid
                if not(index.isValid()):
                    
                    # log
                    self.logger.debug('Index {0} not valid. Continuing.'.format(index))
                    continue
                
                # row
                row = index.row()

                # model
                model = index.model()

                # current_node
                current_node = model.data_list[row][0]

                # check duplicates
                if (id(current_node) in [id(node) for node in node_list]):
                    continue
                
                # append
                node_list.append(current_node)  # column is always zero

        except:
            pass

        return node_list

    # Slots
    # ------------------------------------------------------------------

    @QtCore.Slot()
    def add_selected(self):
        """
        Add selected DAG graph write nodes as
        renderthread nodes to model.
        """

        # nuke_node_list
        nuke_node_list = renderthreads_nuke.get_nodes('Write', True)
        # renderthread_node_list
        renderthread_node_list = renderthreads_nuke.convert_nodes(nuke_node_list)

        try:
            # update
            self.model.add_flat(renderthread_node_list)
        except:
            # log
            self.logger.debug('Error adding renderthread node list from selected DAG nodes to model. Maybe model is not set.')

    @QtCore.Slot()
    def add_all(self):
        """
        Add all DAG graph write nodes as
        renderthread nodes to model.
        """

        # nuke_node_list
        nuke_node_list = renderthreads_nuke.get_nodes('Write')
        # renderthread_node_list
        renderthread_node_list = renderthreads_nuke.convert_nodes(nuke_node_list)

        try:
            # update
            self.model.add_flat(renderthread_node_list)
        except:
            # log
            self.logger.debug('Error adding renderthread node list from all DAG nodes to model. Maybe model is not set.')

    @QtCore.Slot()
    def remove_selected(self):
        """
        Remove selected nodes from model.
        """

        # selected_indices_list
        selected_indices_list = self.get_selected_indices()

        # renderthread_node_list
        renderthread_node_list = self.indices_list_to_node_list(selected_indices_list)

        try:
            # clear
            self.model.remove_data_from_list(renderthread_node_list)
        except:
            # log
            self.logger.debug('Error removing selected nodes from model. Maybe model is not set.')

    @QtCore.Slot()
    def remove_all(self):
        """
        Clear model.
        """

        try:
            # clear
            self.model.clear()
        except:
            # log
            self.logger.debug('Error clearing model. Maybe model is not set.')

    @QtCore.Slot()
    def select_selected(self):
        """
        Select write nodes which are currently
        selected in model.
        """

        try:
            # deselect_all
            renderthreads_nuke.deselect_all()

            # selected_indices_list
            selected_indices_list = self.get_selected_indices()

            # renderthread_node_list
            renderthread_node_list = self.indices_list_to_node_list(selected_indices_list)

            # nuke_node_list
            nuke_node_list = [node.nuke_node for node in renderthread_node_list]

            # select
            renderthreads_nuke.select_nodes(nuke_node_list)
        except:
            # log
            self.logger.debug('Error selecting selected nodes.')

    @QtCore.Slot()
    def select_all(self):
        """
        Select all write nodes in model.
        """

        try:
            # deselect_all
            renderthreads_nuke.deselect_all()

            # renderthread_node_list
            renderthread_node_list = self.model.get_data_list_flat()

            # nuke_node_list
            nuke_node_list = [node.nuke_node for node in renderthread_node_list]

            # select
            renderthreads_nuke.select_nodes(nuke_node_list)
        except:
            # log
            self.logger.debug('Error selecting all nodes.')

    @QtCore.Slot()
    def deselect_all(self):
        """
        Deselect all nodes in scene. Recurse groups.
        """

        try:
            # deselect_all
            renderthreads_nuke.deselect_all()
        except:
            # log
            self.logger.debug('Error deselecting all nodes.')

    '''
    @QtCore.Slot()
    def select_nodes(self):
        """
        Select nodes.
        """

        # selected_indices_list
        selected_indices_list = self.get_selected_indices()
        # pynode_list
        pynode_list = self.indices_list_to_pynode_list(selected_indices_list)
        # clean_pynode_list
        clean_pynode_list = self.asset_manager_functionality.remove_duplicate_pynodes(pynode_list)

        # select
        self.asset_manager_functionality.select_nodes(clean_pynode_list)


    @QtCore.Slot()
    def delete_nodes(self):
        """
        Delete nodes.
        """

        # selected_indices_list
        selected_indices_list = self.get_selected_indices()
        # pynode_list
        pynode_list = self.indices_list_to_pynode_list(selected_indices_list)
        # clean_pynode_list
        clean_pynode_list = self.asset_manager_functionality.remove_duplicate_pynodes(pynode_list)

        # select
        self.asset_manager_functionality.delete_nodes(clean_pynode_list)


    @QtCore.Slot()
    def create_node(self):
        """
        Create node.
        """
    
        # create
        self.asset_manager_functionality.create_node('HelgaShotsMetadata')
    '''
    

    





    # Misc
    # ------------------------------------------------------------------
    def dummy_method(self, msg='dummy'):
        """
        Dummy method.
        """

        # log
        self.logger.debug('{0}'.format(msg))

    def dummy_method_silent(self):
        """
        Dummy method without output.
        """

        pass

    # Test
    # ------------------------------------------------------------------
    def run_tests(self):
        """
        Suite of test methods.
        """

        # log
        self.logger.debug('\n\nExecute test methods:\n-----------------------------')

        # test methods start here
        # ------------------------------------------------------------------
        # ------------------------------------------------------------------

        # dummy_method
        self.dummy_method()

        # ------------------------------------------------------------------
        # ------------------------------------------------------------------
        # test methods end here

        # log
        self.logger.debug('\n\n-----------------------------\nFinished test methods.')