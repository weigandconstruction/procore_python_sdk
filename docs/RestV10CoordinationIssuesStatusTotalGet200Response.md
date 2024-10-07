# RestV10CoordinationIssuesStatusTotalGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_count** | **int** | Count of issues with status &#39;open&#39; | [optional] 
**blocked_count** | **int** | Count of issues with status &#39;blocked&#39; | [optional] 
**unblocked_count** | **int** | Count of issues with status &#39;unblocked&#39; | [optional] 
**ready_for_review_count** | **int** | Count of issues with status &#39;ready_for_review&#39; | [optional] 
**moved_to_observation_count** | **int** | Count of issues with status &#39;moved_to_observation&#39; | [optional] 
**closed_count** | **int** | Count of issues with status &#39;closed&#39; | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_status_total_get200_response import RestV10CoordinationIssuesStatusTotalGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesStatusTotalGet200Response from a JSON string
rest_v10_coordination_issues_status_total_get200_response_instance = RestV10CoordinationIssuesStatusTotalGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesStatusTotalGet200Response.to_json())

# convert the object into a dict
rest_v10_coordination_issues_status_total_get200_response_dict = rest_v10_coordination_issues_status_total_get200_response_instance.to_dict()
# create an instance of RestV10CoordinationIssuesStatusTotalGet200Response from a dict
rest_v10_coordination_issues_status_total_get200_response_from_dict = RestV10CoordinationIssuesStatusTotalGet200Response.from_dict(rest_v10_coordination_issues_status_total_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


