# Lookahead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Lookahead start date, in project time zone | 
**end_date** | **str** | Lookahead end date, in project time zone | 
**copied_from_id** | **int** | ID of a previously created lookahead that will be used to populate this lookahead. Defaults to null, in which case the lookahead will populate directly from the master schedule. | [optional] 

## Example

```python
from procore_sdk.models.lookahead import Lookahead

# TODO update the JSON string below
json = "{}"
# create an instance of Lookahead from a JSON string
lookahead_instance = Lookahead.from_json(json)
# print the JSON string representation of the object
print(Lookahead.to_json())

# convert the object into a dict
lookahead_dict = lookahead_instance.to_dict()
# create an instance of Lookahead from a dict
lookahead_from_dict = Lookahead.from_dict(lookahead_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


