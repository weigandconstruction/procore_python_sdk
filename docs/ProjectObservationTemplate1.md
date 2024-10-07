# ProjectObservationTemplate1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Observation Template ID | [optional] 
**active** | **bool** | Flag denoting if the Observation Template is available for use | [optional] 
**assignee** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**updated_at** | **datetime** | Date updated | [optional] 
**company_observation_template_id** | **int** | Company Observation Template that the Project Observation Template was created from | [optional] 
**observation_title** | **str** | Title to be used for Observations created from this template | [optional] 
**observation_type** | [**ProjectObservationType**](ProjectObservationType.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 

## Example

```python
from procore_sdk.models.project_observation_template1 import ProjectObservationTemplate1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectObservationTemplate1 from a JSON string
project_observation_template1_instance = ProjectObservationTemplate1.from_json(json)
# print the JSON string representation of the object
print(ProjectObservationTemplate1.to_json())

# convert the object into a dict
project_observation_template1_dict = project_observation_template1_instance.to_dict()
# create an instance of ProjectObservationTemplate1 from a dict
project_observation_template1_from_dict = ProjectObservationTemplate1.from_dict(project_observation_template1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


