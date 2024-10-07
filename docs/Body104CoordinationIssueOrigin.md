# Body104CoordinationIssueOrigin

Origin source for a Coordination Issue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the origin item | 
**origin_id** | **str** | Id of the origin item | 
**origin_type** | **str** | Type of origin item | 
**deep_link_url** | **str** | Deep link URL to the origin item | 

## Example

```python
from procore_sdk.models.body104_coordination_issue_origin import Body104CoordinationIssueOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of Body104CoordinationIssueOrigin from a JSON string
body104_coordination_issue_origin_instance = Body104CoordinationIssueOrigin.from_json(json)
# print the JSON string representation of the object
print(Body104CoordinationIssueOrigin.to_json())

# convert the object into a dict
body104_coordination_issue_origin_dict = body104_coordination_issue_origin_instance.to_dict()
# create an instance of Body104CoordinationIssueOrigin from a dict
body104_coordination_issue_origin_from_dict = Body104CoordinationIssueOrigin.from_dict(body104_coordination_issue_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


