# ProjectObservationTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Flag that denotes if the Project Observation Template is available for use | [optional] 
**assignee_id** | **int** | The ID of the Project Observation Template&#39;s Assignee | [optional] 
**trade_id** | **int** | The ID of the Project Observation Template&#39;s Trade | [optional] 

## Example

```python
from procore_sdk.models.project_observation_template import ProjectObservationTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectObservationTemplate from a JSON string
project_observation_template_instance = ProjectObservationTemplate.from_json(json)
# print the JSON string representation of the object
print(ProjectObservationTemplate.to_json())

# convert the object into a dict
project_observation_template_dict = project_observation_template_instance.to_dict()
# create an instance of ProjectObservationTemplate from a dict
project_observation_template_from_dict = ProjectObservationTemplate.from_dict(project_observation_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


