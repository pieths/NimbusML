# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
EnsembleClassifier
"""

__all__ = ["EnsembleClassifier"]


from sklearn.base import ClassifierMixin

from ..base_predictor import BasePredictor
from ..internal.core.ensemble.ensembleclassifier import \
    EnsembleClassifier as core
from ..internal.utils.utils import trace
from .feature_selector import AllFeatureSelector
from .subset_selector import BootstrapSelector


class EnsembleClassifier(core, BasePredictor, ClassifierMixin):
    """

    **Description**
    Train a multi class ensemble model

    .. remarks::
        An Ensemble is a set of models, each trained on a sample of the
        training set. Training an ensemble instead of a single model can boost
        the accuracy of a given algorithm.

        The quality of an Ensemble depends on two factors; Accuracy and
        Diversity. Ensemble can be analogous to Teamwork. If every team member
        is diverse and competent, then the team can perform very well. Here a
        team member is a base learner and the team is the Ensemble. In the case
        of classification ensembles, the base learner is a
        ``LogisticRegressionClassifier``.


    :param feature: see `Columns </nimbusml/concepts/columns>`_.

    :param label: see `Columns </nimbusml/concepts/columns>`_.

    :param sampling_type: Specifies how the training samples are created:

        * ``BootstrapSelector``: takes a bootstrap sample of the training set
          (sampling with replacement). This is the default method.
        * ``RandomPartitionSelector``: randomly partitions the training set
          into subsets.
        * ``AllSelector``: every model is trained using the whole training set.

        Each of these Subset Selectors has two options for selecting features:
        * ``AllFeatureSelector``: selects all the features. This is the default
          method.
        * ``RandomFeatureSelector``: selects a random subset of the features
          for each model.

    :param num_models: indicates the number models to train, i.e. the number of
        subsets of the training set to sample. The default value is 50. If
        batches are used then this indicates the number of models per batch.

    :param sub_model_selector_type: Determines the efficient set of models the
    ``output_combiner`` uses, and removes the least significant models. This is
    used to improve the accuracy and reduce the model size. This is also called
    pruning.

        * ``ClassifierAllSelector``: does not perform any pruning and selects
          all models in the ensemble to combine to create the output. This is
          the default submodel selector.
        * ``ClassifierBestDiverseSelector``: combines models whose predictions
          are as diverse as possible. Currently, only diagreement diversity is
          supported.
        * ``ClassifierBestPerformanceSelector``: combines only the models with
          the best performance according some metric. The metric can be
          ``"AccuracyMicro"``, ``"AccuracyMacro"``,    ``"LogLoss"``,
          or ``"LogLossReduction"``.


    :output_combiner: indicates how to combine the predictions of the different
        models into a single prediction. There are five available output
        combiners for clasification:

        * ``ClassifierAverage``: computes the average of the scores produced by
          the trained models.
        * ``ClassifierMedian``: computes the median of the scores produced by
          the trained models.
        * ``ClassifierStacking``: computes the output by training a model on a
          training set where each instance is a vector containing the outputs
          of the different models on a training instance, and the instance's
          label.
        * ``ClassifierVoting``: computes the fraction of positive predictions
          for each class from all the trained models, and outputs the class
          with the largest number.
        * ``ClassifierWeightedAverage``: computes the weighted average of the
        outputs of the trained models, weighted by the specified metric. The
          metric can be ``"AccuracyMicroAvg"`` or ``"AccuracyMacroAvg"``.

    :param output_combiner: Output combiner.

    :param normalize: Specifies the type of automatic normalization used:

        * ``"Auto"``: if normalization is needed, it is performed
          automatically. This is the default choice.
        * ``"No"``: no normalization is performed.
        * ``"Yes"``: normalization is performed.
        * ``"Warn"``: if normalization is needed, a warning
          message is displayed, but normalization is not performed.

        Normalization rescales disparate data ranges to a standard scale.
        Feature
        scaling ensures the distances between data points are proportional
        and
        enables various optimization methods such as gradient descent to
        converge
        much faster. If normalization is performed, a ``MinMax`` normalizer
        is
        used. It normalizes values in an interval [a, b] where ``-1 <= a <=
        0``
        and ``0 <= b <= 1`` and ``b - a = 1``. This normalizer preserves
        sparsity by mapping zero to zero.

    :param caching: Whether trainer should cache input training data.

    :param train_parallel: All the base learners will run asynchronously if the
        value is true.

    :param batch_size: train the models iteratively on subsets of the training
        set of this size. When using this option, it is assumed that the
        training set is randomized enough so that every batch is a random
        sample of instances. The default value is -1, indicating using the
        whole training set. If the value is changed to an integer greater than
        0, the number of trained models is the number of batches (the size of
        the training set divided by the batch size), times ``num_models``.

    :param show_metrics: True, if metrics for each model need to be evaluated
        and shown in comparison table. This is done by using validation set if
        available or the training set.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        * Subset selectors:
        :py:class:`AllInstanceSelector
        <nimbusml.ensemble.subset_selector.AllInstanceSelector>`,
        :py:class:`BootstrapSelector
        <nimbusml.ensemble.subset_selector.BootstrapSelector>`,
        :py:class:`RandomPartitionSelector
        <nimbusml.ensemble.subset_selector.RandomPartitionSelector>`

        * Feature selectors:
        :py:class:`AllFeatureSelector
        <nimbusml.ensemble.feature_selector.AllFeatureSelector>`,
        :py:class:`RandomFeatureSelector
        <nimbusml.ensemble.feature_selector.RandomFeatureSelector>`

        * Submodel selectors:
        :py:class:`ClassifierAllSelector
        <nimbusml.ensemble.sub_model_selector.ClassifierAllSelector>`,
        :py:class:`ClassifierBestDiverseSelector
        <nimbusml.ensemble.sub_model_selector.ClassifierBestDiverseSelector>`,
        :py:class:`ClassifierBestPerformanceSelector
        <nimbusml.ensemble.sub_model_selector.ClassifierBestPerformanceSelector>`

        * Output combiners:
        :py:class:`ClassifierAverage
        <nimbusml.ensemble.output_combiner.ClassifierAverage>`,
        :py:class:`ClassifierMedian
        <nimbusml.ensemble.output_combiner.ClassifierMedian>`,
        :py:class:`ClassifierStacking
        <nimbusml.ensemble.output_combiner.ClassifierStacking>`,
        :py:class:`ClassifierVoting
        <nimbusml.ensemble.output_combiner.ClassifierVoting>`,
        :py:class:`ClassifierWeightedAverage
        <nimbusml.ensemble.output_combiner.ClassifierWeightedAverage>`


    .. index:: models, ensemble, classification

    Example:
       .. literalinclude:: /../nimbusml/examples/EnsembleClassifier.py
              :language: python
    """

    @trace
    def __init__(
            self,
            sampling_type=BootstrapSelector(
                feature_selector=AllFeatureSelector()),
            num_models=None,
            sub_model_selector_type=None,
            output_combiner=None,
            normalize='Auto',
            caching='Auto',
            train_parallel=False,
            batch_size=-1,
            show_metrics=False,
            feature=None,
            label=None,
            **params):

        if 'feature_column_name' in params:
            raise NameError(
                "'feature_column_name' must be renamed to 'feature'")
        if feature:
            params['feature_column_name'] = feature
        if 'label_column_name' in params:
            raise NameError(
                "'label_column_name' must be renamed to 'label'")
        if label:
            params['label_column_name'] = label
        BasePredictor.__init__(self, type='classifier', **params)
        core.__init__(
            self,
            sampling_type=sampling_type,
            num_models=num_models,
            sub_model_selector_type=sub_model_selector_type,
            output_combiner=output_combiner,
            normalize=normalize,
            caching=caching,
            train_parallel=train_parallel,
            batch_size=batch_size,
            show_metrics=show_metrics,
            **params)
        self.feature = feature
        self.label = label

    @trace
    def predict_proba(self, X, **params):
        '''
        Returns probabilities
        '''
        return self._predict_proba(X, **params)

    @trace
    def decision_function(self, X, **params):
        '''
        Returns score values
        '''
        return self._decision_function(X, **params)

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)