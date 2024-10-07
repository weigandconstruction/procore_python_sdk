# RestV10CoordinationIssuesFilterOptionsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key is the name is the filter field | [optional] 
**value** | **str** | Value is the localized name of the filter field | [optional] 
**endpoint** | **str** | Endpoint is the path to the filter options endpoint | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_filter_options_get200_response_inner import RestV10CoordinationIssuesFilterOptionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesFilterOptionsGet200ResponseInner from a JSON string
rest_v10_coordination_issues_filter_options_get200_response_inner_instance = RestV10CoordinationIssuesFilterOptionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesFilterOptionsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_coordination_issues_filter_options_get200_response_inner_dict = rest_v10_coordination_issues_filter_options_get200_response_inner_instance.to_dict()
# create an instance of RestV10CoordinationIssuesFilterOptionsGet200ResponseInner from a dict
rest_v10_coordination_issues_filter_options_get200_response_inner_from_dict = RestV10CoordinationIssuesFilterOptionsGet200ResponseInner.from_dict(rest_v10_coordination_issues_filter_options_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


