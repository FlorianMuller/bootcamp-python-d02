import React, { ReactElement, useState, useEffect } from "react";
import { useHistory, useLocation } from "react-router-dom";
import { useIntl } from "react-intl";

import CircularProgress from "@material-ui/core/CircularProgress";
import SnackbarContent from "@material-ui/core/SnackbarContent";
import Snackbar from "@material-ui/core/Snackbar";
import Paper from "@material-ui/core/Paper";
import InfiniteScroll from "react-infinite-scroller";

import Thumbnail from "./Thumbnail";
import Film from "./Movie";

import useApi from "../../hooks/useApi";

import { formatQueryUrl } from "./service";

import { useSearchStyles } from "./styles";

const Search = (): ReactElement => {
  const classes = useSearchStyles({});
  const history = useHistory();
  const location = useLocation();
  const { formatMessage: _t } = useIntl();
  const [filmData, setFilmData] = useState(null);
  const [filmList, setFilmList] = useState([]);
  const [block, setBlock] = useState(false);
  const [page, setPage] = useState(1);

  const { data, loading, error, setUrl } = useApi(
    formatQueryUrl(location.search, 1)
  );

  useEffect(() => {
    if (!loading && !block) {
      setPage(1);
      setFilmList([]);
      setUrl(formatQueryUrl(location.search, 1));
    }
  }, [location.search]);

  useEffect(() => {
    if (data?.docs) {
      const docs = data.docs as Record<string, unknown>[];

      setFilmList(() => [...filmList, ...docs]);
      setBlock(false);
    }
  }, [data]);

  const loadMore = (): void => {
    setBlock(true);
    setPage(page + 1);
    setUrl(formatQueryUrl(location.search, page + 1));
  };

  if (error) {
    history.push("/error");
  }

  return (
    <div className={classes.container}>
      <div className={classes.thumbsContainer}>
        <InfiniteScroll
          initialLoad={false}
          useWindow={false}
          loadMore={false}
          hasMore={!block && !loading && page * 10 < data.numFound}
        >
          {filmList.map((film) => (
            <Thumbnail
              key={film.identifier}
              film={film}
              onClick={(): void => history.push(`/movie/${film.identifier}`)}
            />
          ))}
        </InfiniteScroll>
      </div>
      <SnackbarContent
        className={classes.snackbar}
        message={_t(
          { id: "search.film_count" },
          { count: Number(data.numFound || 0) }
        )}
      />
      <Snackbar open={loading} className={classes.snackbarLoading}>
        <SnackbarContent message={_t({ id: "search.loading" })} />
      </Snackbar>
    </div>
  );
};

export default Search;
