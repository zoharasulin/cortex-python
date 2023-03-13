"""
Copyright 2023 Cognitive Scale, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AttributeDataType,
    CampaignLifecycleState,
    ConnectionType,
    ContentType,
    ExplorationType,
    MeasureFrequency,
    MissionLifecycleState,
    PolicyEvaluation,
    ScriptLanguage,
    SinkKind,
    SourceKind,
    TimeoutUnit,
    UserQueryDialectSpec,
    ValueDirection,
)


# pylint: disable=missing-class-docstring
# pylint: disable=empty-docstring

class ResourceRefInput(BaseModel):
    """A reference to a resource"""
    name: str


class AgentActionSpecInput(BaseModel):
    """

    """
    agent: "ResourceRefInput"


class AttributeIdentifierInput(BaseModel):
    """

    """
    name: str
    source_name: str = Field(alias="sourceName")


class AttributeTagInput(BaseModel):
    """

    """
    attributes: List["AttributeIdentifierInput"]
    name: str


class BucketSpecInput(BaseModel):
    """

    """
    filter: str
    name: str


class BucketAttributeSpecInput(BaseModel):
    """

    """
    buckets: List["BucketSpecInput"]
    name: str
    profile_group: Optional[str] = Field(alias="profileGroup")
    source: Optional["ResourceRefInput"]


class CampaignDeleteInput(BaseModel):
    """

    """
    name: str
    project: str


class KPIMeasureSpecInput(BaseModel):
    """

    """
    display_format: Optional[str] = Field(alias="displayFormat")
    expression: str
    is_percentage: bool = Field(alias="isPercentage")
    name: str
    profile_schema: "ResourceRefInput" = Field(alias="profileSchema")


class KPISpecInput(BaseModel):
    """

    """
    cohort_name: str = Field(alias="cohortName")
    description: Optional[str]
    ending_on: Optional[Any] = Field(alias="endingOn")
    frequency: MeasureFrequency
    measure: "KPIMeasureSpecInput"
    name: str
    starting_on: Optional[Any] = Field(alias="startingOn")
    starting_value: Optional[float] = Field(alias="startingValue")
    target_value: Optional[float] = Field(alias="targetValue")
    value_direction: ValueDirection = Field(alias="valueDirection")


class CampaignGoalSpecInput(BaseModel):
    """

    """
    description: Optional[str]
    kpis: List["KPISpecInput"]
    name: str


class CohortGroupSpecInput(BaseModel):
    """

    """
    filter: str
    name: str


class CohortSpecInput(BaseModel):
    """

    """
    groups: List["CohortGroupSpecInput"]
    name: str
    profile_schema: "ResourceRefInput" = Field(alias="profileSchema")


class ConditionSpecInput(BaseModel):
    """

    """
    expression: str
    name: str


class PropertyValueInput(BaseModel):
    """

    """
    name: str
    value: str


class ConnectionInput(BaseModel):
    """

    """
    allow_read: bool = Field(alias="allowRead")
    allow_write: bool = Field(alias="allowWrite")
    connection_type: ConnectionType = Field(alias="connectionType")
    content_type: Optional[ContentType] = Field(alias="contentType")
    description: Optional[str]
    name: str
    params: List["PropertyValueInput"]
    project: str
    title: Optional[str]


class CreateBucketAttributeInput(BaseModel):
    """

    """
    attribute: "BucketAttributeSpecInput"
    profile_schema: str = Field(alias="profileSchema")
    project: str


class CreateCampaignInput(BaseModel):
    """

    """
    description: Optional[str]
    name: str
    project: str
    title: Optional[str]


class CustomAttributeSpecInput(BaseModel):
    """

    """
    expression: str
    name: str
    profile_group: Optional[str] = Field(alias="profileGroup")
    source: Optional["ResourceRefInput"]
    window: Optional[MeasureFrequency]


class CreateCustomAttributeInput(BaseModel):
    """

    """
    attribute: "CustomAttributeSpecInput"
    profile_schema: str = Field(alias="profileSchema")
    project: str


class GoalSpecInput(BaseModel):
    """

    """
    condition: str
    name: str


class SimulatedAttributeInput(BaseModel):
    """

    """
    data_type: AttributeDataType = Field(alias="dataType")
    initial_value: str = Field(alias="initialValue")
    name: str


# pylint: disable=pointless-statement
class ExplorationSpecInput(BaseModel):
    """

    """
    epsilon: Optional[float]
    lambda: Optional[int]
    type: ExplorationType


class SimulationSpecInput(BaseModel):
    """

    """
    attributes: Optional[List[str]]
    exploration: List["ExplorationSpecInput"]
    iterations: int
    limit: Optional[int]
    order: Optional[List[str]]
    policy: List[PolicyEvaluation]
    seed: Optional[int]


class SubjectSpecInput(BaseModel):
    """

    """
    cohort: str


class CreateMissionInput(BaseModel):
    """

    """
    campaign: str
    conditions: Optional[List["ConditionSpecInput"]]
    description: Optional[str]
    goal: "GoalSpecInput"
    name: str
    project: str
    simulated_attributes: Optional[List["SimulatedAttributeInput"]] = Field(
        alias="simulatedAttributes"
    )
    simulation: Optional["SimulationSpecInput"]
    subject: "SubjectSpecInput"
    title: Optional[str]


class ReviewedPlanInput(BaseModel):
    """

    """
    cost: float
    final_rank: int = Field(alias="finalRank")
    ignore: Optional[bool]
    initial_rank: int = Field(alias="initialRank")
    plan_i_d: str = Field(alias="planID")


class CreatePlanReviewInput(BaseModel):
    """

    """
    group_filter: str = Field(alias="groupFilter")
    project: str
    reviewed_plans: List["ReviewedPlanInput"] = Field(alias="reviewedPlans")
    simulation_id: str = Field(alias="simulationId")


class CreateProfileLinkInput(BaseModel):
    """

    """
    linked_profile_attribute: str = Field(alias="linkedProfileAttribute")
    linked_profile_schema: str = Field(alias="linkedProfileSchema")
    profile_attribute: str = Field(alias="profileAttribute")
    profile_schema: str = Field(alias="profileSchema")
    project: str


class CreateProjectInput(BaseModel):
    """

    """
    description: Optional[str]
    name: str
    title: Optional[str]


class DataSinkInput(BaseModel):
    """

    """
    attributes: Optional[List[str]]
    connection: Optional["ResourceRefInput"]
    description: Optional[str]
    kind: SinkKind
    name: str
    project: str
    title: Optional[str]


class UserQueryVariableSpecInput(BaseModel):
    """

    """
    data_type: str = Field(alias="dataType")
    default: Optional[str]
    name: str


class UserQuerySpecInput(BaseModel):
    """

    """
    dialect: UserQueryDialectSpec
    query_string: str = Field(alias="queryString")
    variables: List["UserQueryVariableSpecInput"]


class DataSourceInput(BaseModel):
    """

    """
    attributes: Optional[List[str]]
    connection: Optional["ResourceRefInput"]
    description: Optional[str]
    kind: SourceKind
    name: str
    primary_key: Optional[str] = Field(alias="primaryKey")
    project: str
    query: Optional["UserQuerySpecInput"]
    title: Optional[str]
    user_id: Optional[str] = Field(alias="userId")


class FixedTimestampInput(BaseModel):
    """

    """
    format: Optional[str]
    value: str


class TimestampSpecInput(BaseModel):
    """

    """
    auto: Optional[bool]
    field: Optional[str]
    fixed: Optional["FixedTimestampInput"]
    format: Optional[str]


class DataSourceSelectionInput(BaseModel):
    """

    """
    attributes: Optional[List[str]]
    name: str
    profile_group: Optional[str] = Field(alias="profileGroup")
    profile_key: str = Field(alias="profileKey")
    timestamp: "TimestampSpecInput"


class DeleteBucketAttributeInput(BaseModel):
    """

    """
    attribute_name: str = Field(alias="attributeName")
    profile_schema: str = Field(alias="profileSchema")
    project: str


class DeleteConnectionInput(BaseModel):
    """

    """
    name: str
    project: str


class DeleteCustomAttributeInput(BaseModel):
    """

    """
    attribute_name: str = Field(alias="attributeName")
    profile_schema: str = Field(alias="profileSchema")
    project: str


class DeleteDataSourceInput(BaseModel):
    """

    """
    name: str
    project: str


class DeleteMissionInput(BaseModel):
    """

    """
    campaign: str
    name: str
    project: str


class DeletePlanReviewInput(BaseModel):
    """

    """
    project: str
    review_id: str = Field(alias="reviewId")
    simulation_id: str = Field(alias="simulationId")


class DeleteProfileLinkInput(BaseModel):
    """

    """
    linked_profile_attribute: Optional[str] = Field(alias="linkedProfileAttribute")
    linked_profile_schema: Optional[str] = Field(alias="linkedProfileSchema")
    profile_attribute: Optional[str] = Field(alias="profileAttribute")
    profile_schema: str = Field(alias="profileSchema")
    project: str


class DeleteProfileSchemaInput(BaseModel):
    """

    """
    name: str
    project: str


class EffectSpecInput(BaseModel):
    """

    """
    probability: float
    script: str


class EpsilonGreedySpecInput(BaseModel):
    """

    """
    epsilon: float
    policy: PolicyEvaluation


class FavoriteQueryInput(BaseModel):
    """

    """
    id: Optional[str]
    last_updated: Optional[Any] = Field(alias="lastUpdated")
    profile_schema_id: Optional[str] = Field(alias="profileSchemaId")
    project: Optional[str]
    query: str


class FeatureInput(BaseModel):
    """

    """
    data_type: Optional[str] = Field(alias="dataType")
    description: Optional[str]
    feature_name: str = Field(alias="featureName")
    feature_type: Optional[str] = Field(alias="featureType")
    max_value: Optional[float] = Field(alias="maxValue")
    mean_value: Optional[float] = Field(alias="meanValue")
    min_value: Optional[float] = Field(alias="minValue")
    notes: Optional[str]
    observations: Optional[str]
    pct_dom: Optional[float] = Field(alias="pctDom")
    pct_null: Optional[float] = Field(alias="pctNull")
    profile_group: str = Field(alias="profileGroup")
    project_name: str = Field(alias="projectName")
    source_name: str = Field(alias="sourceName")
    std_dev: Optional[float] = Field(alias="stdDev")
    table_name: str = Field(alias="tableName")
    timestamp: Optional[Any]
    unique_count: Optional[Any] = Field(alias="uniqueCount")


class ScriptActionSpecInput(BaseModel):
    """

    """
    language: ScriptLanguage
    script: str


class SkillActionSpecInput(BaseModel):
    """

    """
    skill: "ResourceRefInput"


class InterventionInput(BaseModel):
    """

    """
    agent_action: Optional["AgentActionSpecInput"] = Field(alias="agentAction")
    condition: Optional[str]
    cost: Optional[float]
    effects: Optional[List["EffectSpecInput"]]
    name: str
    script_action: Optional["ScriptActionSpecInput"] = Field(alias="scriptAction")
    skill_action: Optional["SkillActionSpecInput"] = Field(alias="skillAction")
    timeout: Optional[int]
    timeout_unit: Optional[TimeoutUnit]


class JoinSpecInput(BaseModel):
    """

    """
    join_source_column: str = Field(alias="joinSourceColumn")
    join_type: Optional[str] = Field(alias="joinType")
    primary_source_column: str = Field(alias="primarySourceColumn")


class JoinSourceSelectionInput(BaseModel):
    """

    """
    attributes: Optional[List[str]]
    join: "JoinSpecInput"
    name: str
    profile_group: Optional[str] = Field(alias="profileGroup")
    timestamp: "TimestampSpecInput"


class ListFavoriteQueriesInput(BaseModel):
    """

    """
    profile_schema_id: Optional[str] = Field(alias="profileSchemaId")
    project: Optional[str]


class ProfileNamesInput(BaseModel):
    """

    """
    categories: List[str]
    plural: str
    singular: str
    title: str


class ProfileSchemaInput(BaseModel):
    """

    """
    attribute_tags: Optional[List["AttributeTagInput"]] = Field(alias="attributeTags")
    description: Optional[str]
    joins: Optional[List["JoinSourceSelectionInput"]]
    name: str
    names: "ProfileNamesInput"
    primary_source: "DataSourceSelectionInput" = Field(alias="primarySource")
    project: str
    title: Optional[str]
    user_id: Optional[str] = Field(alias="userId")


class RNDSpecInput(BaseModel):
    """

    """
    alpha: Optional[float]
    epsilon: Optional[float]
    inv_lambda: Optional[float] = Field(alias="invLambda")
    policy: PolicyEvaluation
    predictors: int


class WarmStartSpecInput(BaseModel):
    """

    """
    choices_lambda: Optional[int] = Field(alias="choicesLambda")
    corrupt_prob_warm_start: Optional[float] = Field(alias="corruptProbWarmStart")
    corrupt_type_warm_start: Optional[int] = Field(alias="corruptTypeWarmStart")
    epsilon: float
    full_retrain: bool = Field(alias="fullRetrain")
    interaction: int
    interaction_update: bool = Field(alias="interactionUpdate")
    lambda_scheme: Optional[int] = Field(alias="lambdaScheme")
    learning_rate: Optional[float] = Field(alias="learningRate")
    loss0: Optional[int]
    loss1: Optional[int]
    policy: PolicyEvaluation
    seed: Optional[int]
    validation_split: float = Field(alias="validationSplit")
    warm_start: int = Field(alias="warmStart")
    warm_start_update: bool = Field(alias="warmStartUpdate")


class RefineUsingReviewsInput(BaseModel):
    """

    """
    project: str
    reviews: List[str]
    simulation_id: str = Field(alias="simulationId")
    warm_start_spec: Optional["WarmStartSpecInput"] = Field(alias="warmStartSpec")


class RemoveCampaignGoalInput(BaseModel):
    """

    """
    campaign: str
    goal_name: str = Field(alias="goalName")
    project: str


class RemoveCohortInput(BaseModel):
    """

    """
    campaign: str
    cohort_name: str = Field(alias="cohortName")
    project: str


class RemoveConditionInput(BaseModel):
    """

    """
    campaign: str
    condition_name: str = Field(alias="conditionName")
    mission: str
    project: str


class RemoveInterventionInput(BaseModel):
    """

    """
    campaign: str
    intervention_name: str = Field(alias="interventionName")
    mission: str
    project: str


class RunSimulationInput(BaseModel):
    """

    """
    campaign: str
    mission: str
    project: str
    simulation_spec: Optional["SimulationSpecInput"] = Field(alias="simulationSpec")


class SoftmaxSpecInput(BaseModel):
    """

    """
    lambda: int
    policy: PolicyEvaluation


class SquareCBSpecInput(BaseModel):
    """

    """
    elimination: bool
    gamma_exponent: Optional[int] = Field(alias="gammaExponent")
    gamma_scale: int = Field(alias="gammaScale")
    max_cost: Optional[float] = Field(alias="maxCost")
    mellowness: Optional[float]
    min_cost: Optional[float] = Field(alias="minCost")
    policy: PolicyEvaluation


class RunSimulationV2Input(BaseModel):
    """

    """
    campaign: str
    epsilon_greedy: Optional["EpsilonGreedySpecInput"] = Field(alias="epsilonGreedy")
    mission: str
    project: str
    rnd: Optional["RNDSpecInput"]
    seed: Optional[int]
    softmax: Optional["SoftmaxSpecInput"]
    square_c_b: Optional["SquareCBSpecInput"] = Field(alias="squareCB")
    subject_attributes: Optional[List[str]] = Field(alias="subjectAttributes")
    subject_limit: Optional[int] = Field(alias="subjectLimit")
    subject_order: Optional[List[str]] = Field(alias="subjectOrder")
    training_iterations: Optional[int] = Field(alias="trainingIterations")
    verbose: Optional[bool]


class SaveCampaignGoalInput(BaseModel):
    """

    """
    campaign: str
    goal: "CampaignGoalSpecInput"
    project: str


class SaveCohortInput(BaseModel):
    """

    """
    campaign: str
    cohort: "CohortSpecInput"
    project: str


class SaveConditionInput(BaseModel):
    """

    """
    campaign: str
    condition: "ConditionSpecInput"
    mission: str
    project: str


class SaveInterventionInput(BaseModel):
    """

    """
    campaign: str
    intervention: "InterventionInput"
    mission: str
    project: str


class UpdateBucketAttributeInput(BaseModel):
    """

    """
    attribute: "BucketAttributeSpecInput"
    profile_schema: str = Field(alias="profileSchema")
    project: str


class UpdateCampaignInput(BaseModel):
    """

    """
    description: Optional[str]
    name: str
    project: str
    title: Optional[str]


class UpdateCampaignLifecycleStateInput(BaseModel):
    """

    """
    campaign: str
    new_state: CampaignLifecycleState = Field(alias="newState")
    project: str


class UpdateCustomAttributeInput(BaseModel):
    """

    """
    attribute: "CustomAttributeSpecInput"
    profile_schema: str = Field(alias="profileSchema")
    project: str


class UpdateMissionInput(BaseModel):
    """

    """
    campaign: str
    conditions: Optional[List["ConditionSpecInput"]]
    description: Optional[str]
    goal: Optional["GoalSpecInput"]
    name: str
    project: str
    simulated_attributes: Optional[List["SimulatedAttributeInput"]] = Field(
        alias="simulatedAttributes"
    )
    simulation: Optional["SimulationSpecInput"]
    subject: Optional["SubjectSpecInput"]
    title: Optional[str]


class UpdateMissionLifecycleStateInput(BaseModel):
    """

    """
    campaign: str
    mission: str
    new_state: MissionLifecycleState = Field(alias="newState")
    project: str


class UpdatePlanReviewInput(BaseModel):
    """

    """
    group_filter: str = Field(alias="groupFilter")
    project: str
    review_id: str = Field(alias="reviewId")
    reviewed_plans: List["ReviewedPlanInput"] = Field(alias="reviewedPlans")
    simulation_id: str = Field(alias="simulationId")


class UpdateProjectInput(BaseModel):
    """

    """
    description: Optional[str]
    name: str
    title: Optional[str]


ResourceRefInput.update_forward_refs()
AgentActionSpecInput.update_forward_refs()
AttributeIdentifierInput.update_forward_refs()
AttributeTagInput.update_forward_refs()
BucketSpecInput.update_forward_refs()
BucketAttributeSpecInput.update_forward_refs()
CampaignDeleteInput.update_forward_refs()
KPIMeasureSpecInput.update_forward_refs()
KPISpecInput.update_forward_refs()
CampaignGoalSpecInput.update_forward_refs()
CohortGroupSpecInput.update_forward_refs()
CohortSpecInput.update_forward_refs()
ConditionSpecInput.update_forward_refs()
PropertyValueInput.update_forward_refs()
ConnectionInput.update_forward_refs()
CreateBucketAttributeInput.update_forward_refs()
CreateCampaignInput.update_forward_refs()
CustomAttributeSpecInput.update_forward_refs()
CreateCustomAttributeInput.update_forward_refs()
GoalSpecInput.update_forward_refs()
SimulatedAttributeInput.update_forward_refs()
ExplorationSpecInput.update_forward_refs()
SimulationSpecInput.update_forward_refs()
SubjectSpecInput.update_forward_refs()
CreateMissionInput.update_forward_refs()
ReviewedPlanInput.update_forward_refs()
CreatePlanReviewInput.update_forward_refs()
CreateProfileLinkInput.update_forward_refs()
CreateProjectInput.update_forward_refs()
DataSinkInput.update_forward_refs()
UserQueryVariableSpecInput.update_forward_refs()
UserQuerySpecInput.update_forward_refs()
DataSourceInput.update_forward_refs()
FixedTimestampInput.update_forward_refs()
TimestampSpecInput.update_forward_refs()
DataSourceSelectionInput.update_forward_refs()
DeleteBucketAttributeInput.update_forward_refs()
DeleteConnectionInput.update_forward_refs()
DeleteCustomAttributeInput.update_forward_refs()
DeleteDataSourceInput.update_forward_refs()
DeleteMissionInput.update_forward_refs()
DeletePlanReviewInput.update_forward_refs()
DeleteProfileLinkInput.update_forward_refs()
DeleteProfileSchemaInput.update_forward_refs()
EffectSpecInput.update_forward_refs()
EpsilonGreedySpecInput.update_forward_refs()
FavoriteQueryInput.update_forward_refs()
FeatureInput.update_forward_refs()
ScriptActionSpecInput.update_forward_refs()
SkillActionSpecInput.update_forward_refs()
InterventionInput.update_forward_refs()
JoinSpecInput.update_forward_refs()
JoinSourceSelectionInput.update_forward_refs()
ListFavoriteQueriesInput.update_forward_refs()
ProfileNamesInput.update_forward_refs()
ProfileSchemaInput.update_forward_refs()
RNDSpecInput.update_forward_refs()
WarmStartSpecInput.update_forward_refs()
RefineUsingReviewsInput.update_forward_refs()
RemoveCampaignGoalInput.update_forward_refs()
RemoveCohortInput.update_forward_refs()
RemoveConditionInput.update_forward_refs()
RemoveInterventionInput.update_forward_refs()
RunSimulationInput.update_forward_refs()
SoftmaxSpecInput.update_forward_refs()
SquareCBSpecInput.update_forward_refs()
RunSimulationV2Input.update_forward_refs()
SaveCampaignGoalInput.update_forward_refs()
SaveCohortInput.update_forward_refs()
SaveConditionInput.update_forward_refs()
SaveInterventionInput.update_forward_refs()
UpdateBucketAttributeInput.update_forward_refs()
UpdateCampaignInput.update_forward_refs()
UpdateCampaignLifecycleStateInput.update_forward_refs()
UpdateCustomAttributeInput.update_forward_refs()
UpdateMissionInput.update_forward_refs()
UpdateMissionLifecycleStateInput.update_forward_refs()
UpdatePlanReviewInput.update_forward_refs()
UpdateProjectInput.update_forward_refs()

# pylint: enable=missing-class-docstring
# pylint: enable=empty-docstring
