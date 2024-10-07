# RestV10CoordinationIssuesStatusCountGet200ResponseInner

Coordination Issue Status Count

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **str** | Attribute used for grouping to generate status count | [optional] 
**group_id** | **int** | Id of the field used for grouping. For e.g. if grouped by location, this will be location id | [optional] 
**group_label** | **str** | Value of the field used for aggregation, for e.g. location name | [optional] 
**open_count** | **int** | Count of issues with status &#39;open&#39; | [optional] 
**blocked_count** | **int** | Count of issues with status &#39;blocked&#39; | [optional] 
**unblocked_count** | **int** | Count of issues with status &#39;unblocked&#39; | [optional] 
**ready_for_review_count** | **int** | Count of issues with status &#39;ready_for_review&#39; | [optional] 
**moved_to_observation_count** | **int** | Count of issues with status &#39;moved_to_observation&#39; | [optional] 
**closed_count** | **int** | Count of issues with status &#39;closed&#39; | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_status_count_get200_response_inner import RestV10CoordinationIssuesStatusCountGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesStatusCountGet200ResponseInner from a JSON string
rest_v10_coordination_issues_status_count_get200_response_inner_instance = RestV10CoordinationIssuesStatusCountGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesStatusCountGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_coordination_issues_status_count_get200_response_inner_dict = rest_v10_coordination_issues_status_count_get200_response_inner_instance.to_dict()
# create an instance of RestV10CoordinationIssuesStatusCountGet200ResponseInner from a dict
rest_v10_coordination_issues_status_count_get200_response_inner_from_dict = RestV10CoordinationIssuesStatusCountGet200ResponseInner.from_dict(rest_v10_coordination_issues_status_count_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


