# Default3DesignatedReviewer

Commitment CO Designated Reviewer. This field is only supported for single-tier projects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.default3_designated_reviewer import Default3DesignatedReviewer

# TODO update the JSON string below
json = "{}"
# create an instance of Default3DesignatedReviewer from a JSON string
default3_designated_reviewer_instance = Default3DesignatedReviewer.from_json(json)
# print the JSON string representation of the object
print(Default3DesignatedReviewer.to_json())

# convert the object into a dict
default3_designated_reviewer_dict = default3_designated_reviewer_instance.to_dict()
# create an instance of Default3DesignatedReviewer from a dict
default3_designated_reviewer_from_dict = Default3DesignatedReviewer.from_dict(default3_designated_reviewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


